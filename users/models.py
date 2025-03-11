from django.db import models
from django.contrib.auth.models import AbstractUser
class CustomUser(AbstractUser):
    USER_TYPES = (
        ("startup", "Startup"),
        ("investor", "Investor"),
    )
    username=None
    user_type = models.CharField(max_length=10, choices=USER_TYPES)
    email = models.EmailField(unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["user_type"]
    def __str__(self):
        return f"{self.email} ({self.user_type})"
