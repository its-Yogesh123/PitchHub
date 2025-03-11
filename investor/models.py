from django.db import models
from users.models import CustomUser

class InvestorProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="investor_profile")
    company_name = models.CharField(max_length=255, blank=True, null=True)  # For VC firms
    investment_focus = models.CharField(max_length=100, null=True)  # Example: AI, FinTech
    available_funds = models.DecimalField(max_digits=15, decimal_places=2,null=True)
    def __str__(self):
        return self.user.email
