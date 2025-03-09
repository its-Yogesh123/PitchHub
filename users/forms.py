from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import CustomUser
from startup.models import StartupProfile
from investor.models import InvestorProfile
class CustomUserRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["email", "user_type", "password1", "password2"]

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            if user.user_type == "startup":
                StartupProfile.objects.create(user=user)
            elif user.user_type == "investor":
                InvestorProfile.objects.create(user=user)
        return user
class CustomUserLoginForm(AuthenticationForm):
    username = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={"class": "form-control"}))