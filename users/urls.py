from django.urls import path
from . import views as v
urlpatterns = [
    path('login/',v.login_user),
    path('register/',v.register_user),
    path('dashboard/',v.dashboard),
    path('logout/',v.logout_user),
]
