from django import forms
from .models import Investment
class InvestmentForm(forms.ModelForm):
    class Meta:
        model = Investment
        fields = [
            "amount_invested",
            "investment_type",
            "equity_percentage",
            "additional_notes",
        ]
        widgets = {
            "additional_notes": forms.Textarea(attrs={"rows": 3, "placeholder": "Add any additional details..."}),
        }

    def clean(self):
        cleaned_data = super().clean()
        investment_type = cleaned_data.get("investment_type")
        equity_percentage = cleaned_data.get("equity_percentage")
        if investment_type == "equity" and not equity_percentage:
            self.add_error("equity_percentage", "Equity percentage is required for equity investments.")
        return cleaned_data
