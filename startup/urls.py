from django.urls import path
from . import views
urlpatterns = [
    # path('register/', views.home),
    path('dashboard/',views.startup_dashboard),
]
