from django.contrib import admin, messages
from django.http import HttpResponse
from django.conf import settings
from .models import data
from .Card.GenerateCard import write_text
import os
import pandas as pd
import zipfile
from io import BytesIO

class DataAdmin(admin.ModelAdmin):
    list_display = ('id', 'Reg_no', 'Name', 'fathers_name', 'center_name', 'location', 'grade', 'passing_year', 'Certificate_no', 'Batch', 'Issued_date', 'Certificate', 'profile_image')
    search_fields = ('id', 'Reg_no', 'Name', 'fathers_name', 'center_name', 'location', 'grade', 'passing_year', 'Certificate_no', 'Batch')
    list_filter = ('center_name', 'location', 'grade', 'passing_year', 'Batch', 'Issued_date')

    def generate_certificates(self, request, queryset):
        zip_subdir = "certificates"
        zip_filename = f"{zip_subdir}.zip"
        s = BytesIO()

        with zipfile.ZipFile(s, "w") as zf:
            for obj in queryset:
                try:
                    if obj.Name and not pd.isna(obj.Name):
                        template_path = "C:/Users/Vishal/Desktop/test/test/project/app/Card/certificatedemo.png"
                        if not os.path.exists(template_path):
                            self.message_user(request, f"Template not found: {template_path}", level=messages.ERROR)
                            continue

                        profile_image_path = obj.profile_image.path if obj.profile_image else None

                        certificate_pdf_path = write_text(
                            obj.Reg_no,
                            obj.Certificate_no,
                            obj.Name,
                            obj.fathers_name,
                            obj.center_name,
                            obj.grade,
                            obj.Batch,
                            obj.location,
                            obj.Issued_date,
                            template_path,
                            profile_image_path
                        )

                        if certificate_pdf_path:
                            with open(certificate_pdf_path, "rb") as f:
                                zf.writestr(os.path.basename(certificate_pdf_path), f.read())
                        else:
                            self.message_user(request, f"Failed to generate certificate for {obj.Name}", level=messages.ERROR)

                    else:
                        self.message_user(request, f"Skipping invalid user {obj.Name}", level=messages.ERROR)

                except Exception as e:
                    self.message_user(request, f"Error generating certificate for {obj.Name}: {str(e)}", level=messages.ERROR)

        s.seek(0)
        response = HttpResponse(s, content_type='application/zip')
        response['Content-Disposition'] = f'attachment; filename={zip_filename}'

        self.message_user(request, "Certificates generated successfully.", level=messages.SUCCESS)
        return response

    generate_certificates.short_description = "Generate Certificates"
    actions = [generate_certificates]

admin.site.register(data, DataAdmin)
