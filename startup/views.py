from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from applications.models import ApplicationModel
from .forms import StartupProfileForm
from .models import StartupProfile
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

@login_required
def update_profile(req):
    if(req.method =="POST"):
        form = StartupProfileForm(req.POST)
        if form.is_valid():
            profile=get_object_or_404(StartupProfile,user=req.user)
            profile.company_name=req.POST.get("company_name",profile.company_name)
            profile.industry=req.POST.get("industry",profile.industry)
            profile.website=req.POST.get("website",profile.website)
            profile.save()
            return redirect("/startup/dashboard")
        else:
            return HttpResponse("Invalid Form")
    form = StartupProfileForm()
    return render(req,"startups/set_profile.html",{'form':form})