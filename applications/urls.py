from django.urls import path
from . import views
urlpatterns = [
    path('all/',views.all_applications),
    path('my_application/',views.my_applications),
    path('new/',views.new_application),
]