# urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns
    path('home/indicators', views.indicators_view),
    path('home/ind_create', views.ind_create),
    path('home/ind_delete', views.ind_delete),
    path('home/ind_update', views.ind_update),
    path('home/ind_enable', views.ind_enable),
    path('home/ind_disable', views.ind_disable),

    path('home/scenes', views.scenes_view),
    path('home/sce_create', views.sce_create),
    path('home/sce_delete', views.sce_delete),
    path('home/sce_update', views.sce_update),
    path('home/sce_enable', views.sce_enable),
    path('home/sce_disable', views.sce_disable),
]