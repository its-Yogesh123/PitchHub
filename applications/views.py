from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from startup.models import StartupProfile
from .forms import ApplicationForm
from .models import ApplicationModel
from startup.models import StartupProfile
@login_required
def new_application(request):
    user =request.user
    if user.user_type != "startup":  # Restrict non-startup users
        return redirect("application_list")
    if(request.method == "GET"):
        try:
            startup_profile = StartupProfile.objects.get(user=user)
            if not startup_profile.company_name:
                messages.error(request, "You must complete your startup profile before submitting an application.")
                return redirect('/startup/setprofile')
        except StartupProfile.DoesNotExist:
            messages.error(request, "You must complete your startup profile before submitting an application.")
            return redirect('/startup/setprofile')
    if request.method == "POST":
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.startup = request.user  # Assign logged-in startup
            application.save()
            return redirect("/startup/dashboard")
    form = ApplicationForm()
    return render(request, "applications/new_application.html", {"form": form})
def all_applications(req):
    applications = ApplicationModel.objects.all()
    return render(req,'applications/show_applications.html',{'applications':applications})
@login_required
def my_applications(request):
    applications = ApplicationModel.objects.filter(startup=request.user)
    return render(request, "applications/show_applications.html", {"applications": applications})
@login_required
def application_detail(request, reference_id):
    try:
        application = get_object_or_404(ApplicationModel, reference_id=reference_id, startup=request.user)
    except:
        return HttpResponse("Accesss Denied")
    return render(request, "applications/one_application.html", {"application": application})
@login_required
def delete_application(request, reference_id):
    if request.method == "DELETE":
        application = get_object_or_404(ApplicationModel, reference_id=reference_id)
        if request.user != application.startup:
            return JsonResponse({"error": "Unauthorized access"}, status=403)
        application.delete()
        return JsonResponse({"success": "Application deleted successfully"})
    return JsonResponse({"error": "Invalid request method"}, status=400)