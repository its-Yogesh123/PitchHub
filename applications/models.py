import uuid
from django.db import models
from django.core.validators import FileExtensionValidator
from users.models import CustomUser

class ApplicationModel(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("approved", "Approved"),
        ("rejected", "Rejected"),
    ]

    FUNDING_ROUNDS = [
        ("pre_seed", "Pre-Seed"),
        ("seed", "Seed"),
        ("series_a", "Series A"),
        ("series_b", "Series B"),
        ("series_c", "Series C"),
        ("ipo", "IPO"),
    ]

    TYPE_CHOICES = [
        ("tech", "Tech"),
        ("healthcare", "Healthcare"),
        ("finance", "Finance"),
        ("education", "Education"),
        ("other", "Other"),
    ]

    reference_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    startup = models.ForeignKey(
        CustomUser, 
        on_delete=models.CASCADE, 
        limit_choices_to={"user_type": "startup"}, 
        related_name="startup_applications"
    )
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default="other")  # Type of startup
    funding_round = models.CharField(max_length=20, choices=FUNDING_ROUNDS, default="pre_seed")  # Funding stage
    funding_amount = models.DecimalField(max_digits=15, decimal_places=2)
    
    pitch_deck = models.FileField(
        upload_to="pitch_decks/", 
        blank=True, 
        null=True, 
        validators=[FileExtensionValidator(allowed_extensions=["pdf", "ppt", "pptx"])]
    )  # Only PDFs and PPTs allowed

    business_plan_summary = models.TextField(
        max_length=1000, 
        help_text="Provide a short summary of your business plan (max 1000 characters)"
    )  # Short summary instead of file

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")

    investor_views = models.ManyToManyField(
        CustomUser, 
        related_name="viewed_applications", 
        blank=True, 
        limit_choices_to={"user_type": "investor"}
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def view_count(self):
        return self.investor_views.count()

    def __str__(self):
        return f"Application {self.reference_id} - {self.type} - {self.funding_round} - {self.status}"
