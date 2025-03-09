from django.shortcuts import render
from django.http import JsonResponse
from .models import Investment
def completed_investments(request):
    investments = Investment.objects.filter(status="Completed").values(
        "reference_id", 
        "application__reference_id", 
        "startup__username", 
        "investor__username", 
        "investment_amount", 
        "equity_offered", 
        "timestamp"
    )
    return JsonResponse({"completed_investments": list(investments)})
