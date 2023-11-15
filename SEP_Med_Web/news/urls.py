# urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns
    path('task_center/<int:page>/', views.task_center, name='task_center'),
    path('home/task_center/<int:page>/', views.home_task_center, name='home_task_center'),
    path('task_add/', views.task_add, name='task_add'),
    path('task_del/', views.task_del, name='task_del'),
    path('home/task_add/', views.home_task_add, name='home_task_add'),
    path('upload_image/', views.upload_image, name='upload_image'),
    path('upload_image_page/', views.upload_image_page, name='upload_image_page'),
    path('home/upload_image_page/', views.home_upload_image_page, name='home_upload_image_page'),
    path('reset_task_center/', views.reset_task_center, name='reset_task_center'),
]