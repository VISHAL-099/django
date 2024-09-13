from django.db import models

class data(models.Model):
    id = models.AutoField(primary_key=True)
    Reg_no = models.CharField(max_length=50)
    Name = models.CharField(max_length=100)
    fathers_name = models.CharField(max_length=100)
    center_name = models.CharField(max_length=10)
    location = models.CharField(max_length=40)
    grade = models.CharField(max_length=100)
    passing_year = models.CharField(max_length=100)
    Certificate_no = models.CharField(max_length=100, null=True, blank=True)
    Batch = models.CharField(max_length=50, null=True, blank=True)
    Issued_date = models.DateField()
    Certificate = models.ImageField(upload_to='certificates/', null=True, blank=True)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)


