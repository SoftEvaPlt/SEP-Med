# urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns
    path('auth/login/', views.login_view, name='login'),
    path('auth/logon', views.logon_view, name='logon'),
    path('home/', views.home, name='home'),
    path('task_center/', views.task_center, name='task_center'),
    path('home/task_center/', views.home_task_center, name='home_task_center'),
    path('task_add/', views.task_add, name='task_add'),
    path('home/task_add', views.home_task_add, name='home_task_add'),
]