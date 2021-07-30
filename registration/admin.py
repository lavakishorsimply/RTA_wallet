from django.contrib import admin
from .models import User
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','Name','Driving_License_number','Vehicle_number','Vehicle_color','Month_year_of_manufacture','Insurance_company_name','Insurance_valid_from','Insurance_valid_to','Pending_Challans','Address')
