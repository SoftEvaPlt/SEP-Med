from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views
app_name = "report"

urlpatterns = [
    # Other URL patterns
    path('home/report', views.create_report_view, name='report'),
]

# 添加对媒体文件的处理
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)