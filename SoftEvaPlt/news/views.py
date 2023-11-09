from django.shortcuts import render, redirect
# from django.contrib.auth import login
from .models import User  # 导入自定义用户模型
from .models import Task
from .models import Scene
from .models import TaskStateTable
from .models import SafetyIndicator

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
        user_account = request.POST['user_account']
        password = request.POST['password']
        print(request.POST)
        print(user_account)
        print(password)

        # 使用自定义用户模型进行身份验证
        try:
            user = User.objects.get(user_account=user_account)
            if user.user_password == password:
                # 如果用户名和密码匹配，登录用户
                # login(request, user)
                # 重定向到成功页面或主页
                return redirect('/home/')
            else:
                # 如果密码不匹配，返回到登录页面并显示错误消息
                return render(request, 'news/login.html', {'error_message': '用户名或密码错误'})
        except User.DoesNotExist:
            # 如果找不到具有提供的用户名的用户，返回到登录页面并显示错误消息
            return render(request, 'news/login.html', {'error_message': '未知用户名，请检查用户名或注册账户'})

    return render(request, 'news/login.html')

def logon_view(request):
    return render(request, 'news/logon.html')

def home(request):
    return render(request, 'news/home.html')

def task_center(request):
    all_task_data = Task.objects.all()
    all_task_state_data = TaskStateTable.objects.all()
    if request.method =='POST':
        task_id = request.POST['task_id']
        task_name = request.POST['task_name']
        state_selection = request.POST['dropdownMenu-value']
        start_time = request.POST['start_time']
        end_time = request.POST['end_time']
        print(task_id)
        print(task_name)
        print(state_selection)
        print(start_time)
        print(end_time)
        # 查询
        search_filter = {}
        if task_id:
            search_filter["task_id__contains"] = task_id
        if task_name:
            search_filter["task_name__contains"] = task_name
        #if state_selection:
            # search_filter["task_state__contains"] = state_selection
        if start_time:
            search_filter["task_create_time__gte"] = start_time
        if end_time:
            search_filter["task_create_time__lte"] = end_time
        if search_filter == None:
            search_filter = ""
        all_task_data = Task.objects.filter(**search_filter)


    for task in all_task_data:
        task.task_create_time = task.task_create_time.strftime("%Y-%m-%d %H:%M:%S")
        # task.task_state = task.task_state.task_state_name
    return render(request, 'news/task_center.html', {"task_data": all_task_data, "task_state_data": all_task_state_data})

def home_task_center(request):
    return render(request, 'news/home_task_center.html')

def task_add(request):
    all_scene_data = Scene.objects.all()
    all_si_data = SafetyIndicator.objects.all()

    return render(request, 'news/task_add.html', {"scene_name_data": all_scene_data, "si_category_data": all_si_data})

def home_task_add(request):
    return render(request, 'news/home_task_add.html')
