from django.urls import path

from . import views
app_name = "report"

urlpatterns = [
    # Other URL patterns
    path('home/report', views.create_report_view, name='report'),
]