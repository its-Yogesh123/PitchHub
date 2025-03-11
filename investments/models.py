from django.db import models
from users.models import CustomUser
from applications.models import ApplicationModel
import uuid
class Investment(models.Model):
    INVESTMENT_TYPES = [
        ("equity", "Equity"),
        ("debt", "Debt"),
        ("grant", "Grant"),
        ("other", "Other"),
    ]

    STATUS_CHOICES = [
        ("pending", "Pending Verification"),
        ("approved", "Approved"),
        ("rejected", "Rejected"),
    ]

    investment_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    application = models.OneToOneField(
        ApplicationModel, 
        on_delete=models.CASCADE, 
        related_name="investment"
    )  # Link to the approved application

    investor = models.ForeignKey(
        CustomUser, 
        on_delete=models.CASCADE, 
        limit_choices_to={"user_type": "investor"}, 
        related_name="investor_investments"
    )

    startup = models.ForeignKey(
        CustomUser, 
        on_delete=models.CASCADE, 
        limit_choices_to={"user_type": "startup"}, 
        related_name="startup_funding"
    )  

    amount_invested = models.DecimalField(max_digits=15, decimal_places=2)
    investment_type = models.CharField(max_length=10, choices=INVESTMENT_TYPES, default="equity")
    equity_percentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")  # New field for verification process
    timestamp = models.DateTimeField(auto_now_add=True)  #When investment was created
    verified_at = models.DateTimeField(null=True, blank=True)  #When startup verifies investment
    additional_notes = models.TextField(blank=True, null=True)
    def __str__(self):
        return f"Investment {self.investment_id} - {self.status}"