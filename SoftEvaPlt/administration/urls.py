# urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns
    path('admin/', views.admin_view),
    path('admin/indicators', views.indicators_view),
    path('admin/ind_create', views.ind_create),
    path('admin/ind_update', views.ind_update),
    path('admin/ind_enable', views.ind_enable),
    path('admin/ind_disable', views.ind_disable),
    path('admin/ind_delete', views.ind_delete),

    path('admin/scenes', views.scenes_view),
    path('admin/sce_create', views.sce_create),
    path('admin/sce_update', views.sce_update),
    path('test', views.test)
]