from django.shortcuts import render
from .forms import RegistrationForm,LoginForm
from .models import User
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.hashers import make_password,check_password
from django.db.models import Max

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user_account = form.cleaned_data['user_account']
            user_password = form.cleaned_data['user_password']

            # 查询用户
            try:
                user = User.objects.get(user_account=user_account)
            except User.DoesNotExist:
                user = None

            # 验证用户的密码
            if user and check_password(user_password, user.user_password):
                # 登录用户
                # login(request, user) TODO'缺少last_login的字段，看后续是否要记录用户的登录状态'
                # 登录成功后的逻辑，例如重定向到特定页面
                return redirect('/home/task_center/1/')
            else:
                # 登录失败的逻辑，例如错误提示
                error_message = "用户名或密码不正确"
                return render(request, 'users/login.html', {'form': form, 'error_message': error_message})
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user_account = form.cleaned_data['user_account']
            user_password = form.cleaned_data['user_password']
            confirm_password = form.cleaned_data['confirm_password']
            user_name = form.cleaned_data['user_name']
            # 检查用户两次输入的密码是否一致 TODO 不知道为什么这个判断不能成功回显在前端
            # if confirm_password != user_password:
            #     error_message = "两次输入的密码不一致。"
            #     return render(request, 'users/register.html', {'form': form, 'error_message': error_message})
            
            # 检查数据库中是否已存在相同的用户账号
            existing_user = User.objects.filter(user_account=user_account).exists()
            existing_name = User.objects.filter(user_account=user_name).exists()
            if existing_user:
                # 如果存在相同账号，显示错误信息
                error_message = "该账号已经存在，请输入另一个账号。"
                return render(request, 'users/register.html', {'form': form, 'error_message': error_message})
            elif existing_name:
                error_message = "该用户名已经存在，请输入另一个账号。"
                return render(request, 'users/register.html', {'form': form, 'error_message': error_message})
            else:
                print(form.cleaned_data)
                max_user_id = User.objects.aggregate(Max('user_id'))['user_id__max']
                next_user_id = max_user_id + 1 if max_user_id else 1
                user = User(
                    user_account = user_account,
                    # 对密码进行加密处理
                    user_password = make_password(user_password),
                    user_name = form.cleaned_data['user_name'],
                    user_email = form.cleaned_data['user_email'],
                    user_phone = form.cleaned_data['user_phone'],
                    user_id = next_user_id,
                    user_authority = 0
                )
                print(user_password)
                user.save()
                # 可以添加其他逻辑，比如注册成功后的重定向或信息提示
                return redirect('/home/task_center/1/')
    else:
        # error_message = "注册错误"
        form = RegistrationForm()
        return render(request, 'users/register.html', {'form': form})
        
    return render(request, 'users/register.html', {'form': form})



# import logging
# from django.utils.translation import gettext_lazy as _
# from django.conf import settings
# from django.contrib import auth
# from django.contrib.auth import REDIRECT_FIELD_NAME
# from django.contrib.auth import get_user_model
# from django.contrib.auth import logout
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth.hashers import make_password
# from django.http import HttpResponseRedirect, HttpResponseForbidden
# from django.http.request import HttpRequest
# from django.http.response import HttpResponse
# from django.shortcuts import get_object_or_404
# from django.shortcuts import render
# from django.urls import reverse
# from django.utils.decorators import method_decorator
# from django.utils.http import url_has_allowed_host_and_scheme
# from django.views import View
# from django.views.decorators.cache import never_cache
# from django.views.decorators.csrf import csrf_protect
# from django.views.decorators.debug import sensitive_post_parameters
# from django.views.generic import FormView, RedirectView

# from .utils import send_email, get_sha256, get_current_site, generate_code
# from . import utils
# from .forms import RegisterForm, LoginForm
# from .models import User

# logger = logging.getLogger(__name__)


# # Create your views here.

# class RegisterView(FormView):
#     form_class = RegisterForm
#     template_name = 'users/register.html'

#     @method_decorator(csrf_protect)
#     def dispatch(self, *args, **kwargs):
#         return super(RegisterView, self).dispatch(*args, **kwargs)

#     def form_valid(self, form):
#         if form.is_valid():
#             user = form.save(False)
#             user.is_active = False
#             user.source = 'Register'
#             user.save(True)
#             site = get_current_site().domain
#             sign = get_sha256(get_sha256(settings.SECRET_KEY + str(user.id)))

#             if settings.DEBUG:
#                 site = '127.0.0.1:8000'
#             path = reverse('account:result')
#             url = "http://{site}{path}?type=validation&id={id}&sign={sign}".format(
#                 site=site, path=path, id=user.id, sign=sign)

#             content = """
#                             <p>请点击下面链接验证您的邮箱</p>

#                             <a href="{url}" rel="bookmark">{url}</a>

#                             再次感谢您！
#                             <br />
#                             如果上面链接无法打开，请将此链接复制至浏览器。
#                             {url}
#                             """.format(url=url)
#             send_email(
#                 emailto=[
#                     user.email,
#                 ],
#                 title='验证您的电子邮箱',
#                 content=content)

#             url = reverse('accounts:result') + \
#                   '?type=register&id=' + str(user.id)
#             return HttpResponseRedirect(url)
#         else:
#             return self.render_to_response({
#                 'form': form
#             })


# class LogoutView(RedirectView):
#     url = '/login/'

#     @method_decorator(never_cache)
#     def dispatch(self, request, *args, **kwargs):
#         return super(LogoutView, self).dispatch(request, *args, **kwargs)

#     def get(self, request, *args, **kwargs):
#         logout(request)
#         # delete_sidebar_cache()
#         return super(LogoutView, self).get(request, *args, **kwargs)


# class LoginView(FormView):
#     form_class = LoginForm
#     template_name = 'users/login.html' #‘users/login/’
#     success_url = '/'
#     redirect_field_name = REDIRECT_FIELD_NAME
#     login_ttl = 2626560  # 一个月的时间

#     @method_decorator(sensitive_post_parameters('password'))
#     @method_decorator(csrf_protect)
#     @method_decorator(never_cache)
#     def dispatch(self, request, *args, **kwargs):

#         return super(LoginView, self).dispatch(request, *args, **kwargs)

#     def get_context_data(self, **kwargs):
#         redirect_to = self.request.GET.get(self.redirect_field_name)
#         if redirect_to is None:
#             redirect_to = 'users/home.html'
#         kwargs['redirect_to'] = redirect_to

#         return super(LoginView, self).get_context_data(**kwargs)

#     def form_valid(self, form):
#         form = AuthenticationForm(data=self.request.POST, request=self.request)

#         if form.is_valid():
#             # delete_sidebar_cache()
#             logger.info(self.redirect_field_name)

#             auth.login(self.request, form.get_user())
#             if self.request.POST.get("remember"):
#                 self.request.session.set_expiry(self.login_ttl)
#             return super(LoginView, self).form_valid(form)
#             # return HttpResponseRedirect('/')
#         else:
#             return self.render_to_response({
#                 'form': form
#             })

#     def get_success_url(self):

#         redirect_to = self.request.POST.get(self.redirect_field_name)
#         if not url_has_allowed_host_and_scheme(
#                 url=redirect_to, allowed_hosts=[
#                     self.request.get_host()]):
#             redirect_to = self.success_url
#         return redirect_to


# def account_result(request):
#     type = request.GET.get('type')
#     id = request.GET.get('id')

#     user = get_object_or_404(get_user_model(), id=id)
#     logger.info(type)
#     if user.is_active:
#         return HttpResponseRedirect('/')
#     if type and type in ['register', 'validation']:
#         if type == 'register':
#             content = '''
#     恭喜您注册成功，一封验证邮件已经发送到您的邮箱，请验证您的邮箱后登录本站。
#     '''
#             title = '注册成功'
#         else:
#             c_sign = get_sha256(get_sha256(settings.SECRET_KEY + str(user.id)))
#             sign = request.GET.get('sign')
#             if sign != c_sign:
#                 return HttpResponseForbidden()
#             user.is_active = True
#             user.save()
#             content = '''
#             恭喜您已经成功的完成邮箱验证，您现在可以使用您的账号来登录本站。
#             '''
#             title = '验证成功'
#         return render(request, 'account/result.html', {
#             'title': title,
#             'content': content
#         })
#     else:
#         return HttpResponseRedirect('/')


# class ForgetPasswordView(FormView):
#     form_class = ForgetPasswordForm
#     template_name = 'account/forget_password.html'

#     def form_valid(self, form):
#         if form.is_valid():
#             user = User.objects.filter(email=form.cleaned_data.get("email")).get()
#             user.password = make_password(form.cleaned_data["new_password2"])
#             user.save()
#             return HttpResponseRedirect('/login/')
#         else:
#             return self.render_to_response({'form': form})


# class ForgetPasswordEmailCode(View):

#     def post(self, request: HttpRequest):
#         form = ForgetPasswordCodeForm(request.POST)
#         if not form.is_valid():
#             return HttpResponse("错误的邮箱")
#         to_email = form.cleaned_data["email"]

#         code = generate_code()
#         utils.send_verify_email(to_email, code)
#         utils.set_code(to_email, code)

#         return HttpResponse("ok")