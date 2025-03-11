from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from .models import InvestorProfile
from .forms import InvestorProfileForm
from applications.models import ApplicationModel
from startup.models import StartupProfile
# Create your views here.
def investor_dashboard(req):
    return render(req,'investors/dashboard.html')
@login_required
def explore_startup(request):
    applications=ApplicationModel.objects.all()
    return render(request, "investors/application.html", {"applications": applications})
@login_required
def update_profile(request):
    user=request.user
    try:
        investor_profile=InvestorProfile.objects.get(user=request.user)
    except:
        return HttpResponse("Something Went Wrong in Update Profile")
    if(user.user_type != "investor"):
        return redirect("/")
    if request.method=="POST":
        form =InvestorProfileForm(request.POST,instance=investor_profile)
        if form.is_valid():
            form.save()
            return redirect("/investor/dashboard")
    form =InvestorProfileForm()
    return render(request,"investors/set_profile.html",{'form':form})
    