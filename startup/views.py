from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from applications.models import ApplicationModel
@login_required
def startup_dashboard(request):
    # Fetch applications for the logged-in startup
    applications = ApplicationModel.objects.filter(startup=request.user)
    total_applications = applications.count()
    pending_applications = applications.filter(status="pending").count()
    approved_applications = applications.filter(status="approved").count()
    rejected_applications = applications.filter(status="rejected").count()

    context = {
        "total_applications": total_applications,
        "pending_applications": pending_applications,
        "approved_applications": approved_applications,
        "rejected_applications": rejected_applications,
    }

    return render(request, "startups/dashboard.html", {'context':context})
