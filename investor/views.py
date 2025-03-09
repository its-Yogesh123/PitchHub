from django.shortcuts import render

# Create your views here.
def investor_dashboard(req):
    return render(req,'investors/dashboard.html')