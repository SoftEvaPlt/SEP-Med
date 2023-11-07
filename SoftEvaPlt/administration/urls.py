# urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns
    path('admin/', views.admin_view),
    path('admin/indicators', views.indicators_view),
    path('admin/scenes', views.scenes_view),
    path('admin/new_indicator', views.new_indicator)
]