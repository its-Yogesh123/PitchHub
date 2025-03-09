from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserRegistrationForm, CustomUserLoginForm
# Register a new user
def register_user(request):
    if request.method == "POST":
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # return redirect("/")  # Redirect to startup/investor dashboard
            return HttpResponse("User Created") 
    else:
        form = CustomUserRegistrationForm()
    return render(request, "users/registration.html", {"form": form})

# Login user
def login_user(request):
    if request.method == "POST":
        form = CustomUserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # return redirect("dashboard")  # Redirect to dashboard
            return HttpResponse("Logged In")
    else:
        form = CustomUserLoginForm()
    return render(request, "users/login.html", {"form": form})

# Logout user
def logout_user(request):
    logout(request)
    return redirect("login")
