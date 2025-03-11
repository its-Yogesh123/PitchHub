from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserRegistrationForm, CustomUserLoginForm
# Register a new user
def register_user(request):
    if(request.user.is_authenticated):
        return redirect("/user/dashboard")
    if request.method == "POST":
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/user/dashboard")
    else:
        form = CustomUserRegistrationForm()
    return render(request, "users/registration.html", {"form": form})

# Login user
def login_user(request):
    if(request.user.is_authenticated):
        return redirect("/user/dashboard")
    if request.method == "POST":
        form = CustomUserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("/user/dashboard")  # Redirect to dashboard
    else:
        form = CustomUserLoginForm()
    return render(request, "users/login.html", {"form": form})
@login_required
def dashboard(request):
    user = request.user  # Ensure we access the actual user object
    if(user.user_type == 'startup'):
        return redirect("/startup/dashboard")
    else :
        return redirect("/investor/dashboard")
# Logout user
@login_required
def logout_user(request):
    logout(request)
    return redirect("/")
