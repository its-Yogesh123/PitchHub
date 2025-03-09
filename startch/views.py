from django.shortcuts import render
# from startups.models import Start
# from investors.models import Investor
from applications.models import ApplicationModel
from investments.models import Investment

def home(request):
    """Landing page displaying site statistics"""
    total_applications = ApplicationModel.objects.count()
    total_startups = total_applications
    total_investors = total_applications
    total_investments = total_applications

    context = {
        "total_startups": total_startups,
        "total_investors": total_investors,
        "total_applications": total_applications,
        "total_investments": total_investments,
    }
    
    return render(request, "index.html", {'context':context})
