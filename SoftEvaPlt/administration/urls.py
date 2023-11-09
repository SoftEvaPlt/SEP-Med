# urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns
    path('admin/', views.admin_view),
    path('admin/indicators', views.indicators_view),
    path('admin/ind_create', views.ind_create),
    path('admin/ind_update', views.ind_update),
    path('admin/scenes', views.scenes_view),
    path('admin/sce_create', views.sce_create),
    path('admin/sce_update', views.sce_update),
]