from .models import InvestorProfile
from django import forms
class InvestorProfileForm(forms.ModelForm):
    class Meta:
        model = InvestorProfile
        fields = ['company_name', 'investment_focus', 'available_funds']
        labels = {
            'company_name': 'Company Name (Optional)',
            'investment_focus': 'Investment Focus (e.g., AI, FinTech)',
            'available_funds': 'Available Funds (USD)',
        }
        widgets = {
            'investment_focus': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your focus area'}),
            'available_funds': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter available funds'}),
        }
