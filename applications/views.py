from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .forms import ApplicationForm
from .models import ApplicationModel
@login_required
def new_application(request):
    if request.user.user_type != "startup":  # Restrict non-startup users
        return redirect("application_list")  
    if request.method == "POST":
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.startup = request.user  # Assign logged-in startup
            application.save()
            return redirect("/startup/dashboard")
    else:
        form = ApplicationForm()
    return render(request, "applications/new_application.html", {"form": form})
def all_applications(req):
    applications = ApplicationModel.objects.all()
    return render(req,'applications/show_application.html',{'applications':applications})
@login_required
def my_applications(request):
    applications = ApplicationModel.objects.filter(startup=request.user)
    return render(request, "applications/show_applications.html", {"applications": applications})
@login_required
def application_detail(request, reference_id):
    application = get_object_or_404(ApplicationModel, reference_id=reference_id, startup=request.user)
    return render(request, "applications/application_detail.html", {"application": application})
@login_required
def delete_application(request, reference_id):
    if request.method == "DELETE":
        application = get_object_or_404(ApplicationModel, reference_id=reference_id)
        if request.user != application.startup:
            return JsonResponse({"error": "Unauthorized access"}, status=403)
        application.delete()
        return JsonResponse({"success": "Application deleted successfully"})
    return JsonResponse({"error": "Invalid request method"}, status=400)
