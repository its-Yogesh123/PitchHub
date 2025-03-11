from django.shortcuts import render
# from startups.models import Start
# from investors.models import Investor
from applications.models import ApplicationModel
from users.models import CustomUser
from investments.models import Investment
from django.db.models import Sum
def home(request):
    """Landing page displaying site statistics"""
    total_applications = ApplicationModel.objects.count()
    total_startups = CustomUser.objects.filter(user_type="startup").count()
    total_investors = CustomUser.objects.filter(user_type="investor").count()
    total_investments = Investment.objects.aggregate(total=Sum("amount_invested"))["total"]
    context = {
        "total_startups": total_startups,
        "total_investors": total_investors,
        "total_applications": total_applications,
        "total_investments": total_investments,
    }
    
    return render(request, "index.html", {'context':context})
