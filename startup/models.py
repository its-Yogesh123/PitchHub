from django.db import models
from users.models import CustomUser
class StartupProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="startup_profile")
    company_name = models.CharField(max_length=255)
    industry = models.CharField(max_length=100)
    website = models.URLField(blank=True, null=True)
    def __str__(self):
        return self.company_name
