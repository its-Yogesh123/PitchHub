from django import forms
from .models import StartupProfile
class StartupProfileForm(forms.ModelForm):
    class Meta:
        model = StartupProfile
        fields = ['company_name', 'industry', 'website']  # Fields to include in the form
        widgets = {
            'company_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter company name'}),
            'industry': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter industry'}),
            'website': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter website URL'}),
        }
