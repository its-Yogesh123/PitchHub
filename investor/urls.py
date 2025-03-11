from django.urls import path
from . import views
urlpatterns = [
    path('dashboard/', views.investor_dashboard),
    path('explore/', views.explore_startup),
    path('update_profile/', views.update_profile),
]
