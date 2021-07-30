from django.db import models

from django import forms
class User(models.Model):
    Name = models.CharField(max_length=30)
    Driving_License_number = models.CharField(max_length=15)
    Vehicle_number = models.CharField(max_length=10)
    Vehicle_color = models.CharField(max_length=10)
    Month_year_of_manufacture = models.DateField()
    Insurance_company_name = models.CharField(max_length=20)
    Insurance_valid_from = models.DateField()
    Insurance_valid_to = models.DateField()
    Pending_Challans =  models.IntegerField()
    Address = models.TextField()
