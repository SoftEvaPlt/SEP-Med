from django.urls import path
from django.urls import re_path

from . import views
# from .forms import LoginForm
app_name = "users"

urlpatterns = [
    path('auth/login/', views.login_view, name='login'),
    path('auth/register/', views.register_view, name='register'),
]