from django.shortcuts import render, redirect
# from django.contrib.auth import login
from .models import User  # 导入自定义用户模型

'''
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username)
        print(password)

        # 使用自定义用户模型进行身份验证
        try:
            user = User.objects.get(user_account=username)
            if user.user_password == password:
                # 如果用户名和密码匹配，登录用户
                # login(request, user)
                # 重定向到成功页面或主页
                return redirect('https://www.baidu.com/')
            else:
                # 如果密码不匹配，返回到登录页面并显示错误消息
                return render(request, 'news/login.html', {'error_message': 'Invalid login credentials'})
        except User.DoesNotExist:
            # 如果找不到具有提供的用户名的用户，返回到登录页面并显示错误消息
            return render(request, 'news/login.html', {'error_message': 'User not found'})

    return render(request, 'news/login.html')
'''

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(request.POST)
        print(username)
        print(password)

        # 使用自定义用户模型进行身份验证
        try:
            user = User.objects.get(user_account=username)
            if user.user_password == password:
                # 如果用户名和密码匹配，登录用户
                # login(request, user)
                # 重定向到成功页面或主页
                return redirect('https://www.baidu.com/')
            else:
                # 如果密码不匹配，返回到登录页面并显示错误消息
                return render(request, 'news/login.html', {'error_message': '用户名或密码错误'})
        except User.DoesNotExist:
            # 如果找不到具有提供的用户名的用户，返回到登录页面并显示错误消息
            return render(request, 'news/login.html', {'error_message': '未知用户名，请检查用户名或注册账户'})

    return render(request, 'news/login.html')

def home(request):
    return render(request, 'news/home.html')