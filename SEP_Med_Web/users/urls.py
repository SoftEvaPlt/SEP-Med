from django.urls import path
from django.urls import re_path

from . import views
# from .forms import LoginForm
app_name = "users"

urlpatterns = [
    # Other URL patterns
    # path('auth/login/', views.LoginView.as_view(), name='login'),
    # path('auth/register/', views.RedirectView.as_view(), name='register'),
    path('auth/login/', views.login_view, name='login'),
    path('auth/register/', views.register_view, name='register'),
    path('home/', views.home, name='home'),
#     path('home/', views.home, name='home'),
# re_path(r'^login/$',
#                        views.LoginView.as_view(success_url='/'),
#                        name='login',
#                        kwargs={'authentication_form': LoginForm}),
#                re_path(r'^register/$',
#                        views.RegisterView.as_view(success_url="/"),
#                        name='register'),
#                re_path(r'^logout/$',
#                        views.LogoutView.as_view(),
#                        name='logout'),
#                path(r'account/result.html',
#                     views.account_result,
#                     name='result'),
#                re_path(r'^forget_password/$',
#                        views.ForgetPasswordView.as_view(),
#                        name='forget_password'),
#                re_path(r'^forget_password_code/$',
#                        views.ForgetPasswordEmailCode.as_view(),
#                        name='forget_password_code'),
               ]