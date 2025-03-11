from django import forms
from .models import ApplicationModel

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = ApplicationModel
        fields = [
            "type", 
            "funding_round", 
            "funding_amount", 
            "pitch_deck", 
            "business_plan_summary"
        ]
        widgets = {
            "business_plan_summary": forms.Textarea(attrs={"rows": 4, "placeholder": "Explain Short Summary about Startup..."}),
        }
    def clean_pitch_deck(self):
        pitch_deck = self.cleaned_data.get("pitch_deck")
        if pitch_deck and pitch_deck.name.split(".")[-1] not in ["pdf", "ppt", "pptx"]:
            raise forms.ValidationError("Only PDF and PPT files are allowed.")
        return pitch_deck
