from django.core import validators
from django import forms
from.models import User
# from django.forms import ModelForm

class RTA_registration(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'Name': forms.TextInput(attrs={'class':'form-control'}),
            'Driving_License_number': forms.TextInput(attrs={'class': 'form-control'}),
            'Vehicle_number': forms.TextInput(attrs={'class': 'form-control'}),
            'Vehicle_color': forms.TextInput(attrs={'class': 'form-control'}),
            'Month_year_of_manufacture': forms.TextInput(attrs={'class': 'form-control'}),
            'Insurance_company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'Insurance_valid_from': forms.TextInput(attrs={'class': 'form-control'}),
            'Insurance_valid_to': forms.TextInput(attrs={'class': 'form-control'}),
            'Pending_Challans': forms.TextInput(attrs={'class': 'form-control'}),
            'Address': forms.TextInput(attrs={'class': 'form-control'}),

        }




