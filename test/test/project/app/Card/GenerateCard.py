import cv2
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from fpdf import FPDF
from django.conf import settings

def add_text_to_image(image, text, position, font, font_color):
    pil_image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(pil_image)
    x, y = position
    draw.text((x, y), text, font=font, fill=font_color)
    return cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)

def add_image_to_certificate(certificate_image, profile_image_path, position, size):
    profile_image = Image.open(profile_image_path).resize(size)
    profile_image = np.array(profile_image)

    if profile_image.shape[2] == 4:
        profile_image = profile_image[:, :, :3]

    x, y = position
    certificate_image[y:y+profile_image.shape[0], x:x+profile_image.shape[1]] = profile_image
    return certificate_image

def write_text(Reg_no, Certificate_no, Name, fathers_name, center_name, grade, Batch, location, Issued_date, TEMPLATE_PATH, profile_image_path):
    image = cv2.imread(TEMPLATE_PATH)
    if image is None:
        print(f"Failed to read image from path: {TEMPLATE_PATH}")
        return None

    font_color = (0, 0, 0)
    font_path = "C:/Users/Vishal/Desktop/test/test/project/app/Card/MartianMono_SemiCondensed-Regular.ttf"

    if not os.path.exists(font_path):
        print(f"Font file not found: {font_path}")
        return None

    font_sizes = {
        'Reg_no': 55,
        'Certificate_no': 55,
        'Name': 50,
        'fathers_name': 50,
        'center_name': 50,
        'grade': 50,
        'Batch': 50,
        'location': 50,
        'Issued_date': 50
    }

    try:
        fonts = {key: ImageFont.truetype(font_path, size=value) for key, value in font_sizes.items()}
    except IOError as e:
        print(f"Error loading font: {e}")
        return None

    positions = {
        'Reg_no': (700, 200),
        'Certificate_no': (2000, 200),
        'Name': (1300, 1210),
        'fathers_name': (1300, 1320),
        'center_name': (941, 1660),
        'grade': (600, 1890),
        'Batch': (1300, 1890),
        'profile_image': (410, 2220),
        'location': (941, 1770),
        'Issued_date': (410, 3260)
    }

    # Convert Issued_date to string
    Issued_date_str = Issued_date.strftime('%Y-%m-%d')

    for key, pos in positions.items():
        if key == 'profile_image':
            continue
        text = eval(key) if key != 'Issued_date' else Issued_date_str
        image = add_text_to_image(image, text, pos, fonts[key], font_color)

    if profile_image_path and os.path.exists(profile_image_path):
        image = add_image_to_certificate(image, profile_image_path, positions['profile_image'], (335, 405))
    else:
        print(f"Profile image not found: {profile_image_path}")

    certificate_directory = os.path.join(settings.STATIC_ROOT, 'certificate')
    os.makedirs(certificate_directory, exist_ok=True)
    certificate_image_path = os.path.join(certificate_directory, f"{Name}_certificate.png")
    cv2.imwrite(certificate_image_path, image)

    pdf = FPDF()
    pdf.add_page()
    pdf.image(certificate_image_path, x=0, y=0, w=210, h=297)
    certificate_pdf_path = os.path.join(certificate_directory, f"{Name}_certificate.pdf")
    pdf.output(certificate_pdf_path)

    os.remove(certificate_image_path)

    return certificate_pdf_path
