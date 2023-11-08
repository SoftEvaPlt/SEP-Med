# urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns
    path('auth/login/', views.login_view, name='login'),
    path('home/', views.home, name='home'),
]