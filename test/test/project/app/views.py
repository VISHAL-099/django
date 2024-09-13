import pandas as pd
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import data
from .forms import UploadFileForm

def upload_excel(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            try:
                df = pd.read_excel(file, engine='openpyxl')
                for index, row in df.iterrows():
                    data.objects.create(
                        id=row['id'],
                        Reg_no=row['Reg_no'],
                        Name=row['Name'],
                        fathers_name=row['fathers_name'],
                        center_name=row['center_name'],
                        location=row['location'],
                        grade=row['grade'],
                        passing_year=row['passing_year'],
                        Certificate_no=row.get('Certificate_no', None),
                        Batch=row.get('Batch', None),
                        Issued_date=row['Issued_date'],
                        Certificate=row.get('Certificate', None),
                        profile_image=row.get('profile_image', None)  # Assuming profile_image is also included in the excel file
                    )
                messages.success(request, 'Data uploaded successfully')
            except Exception as e:
                messages.error(request, f'Error uploading data: {e}')
            return redirect('upload_excel')
    else:
        form = UploadFileForm()
    return render(request, 'upload_excel.html', {'form': form})
