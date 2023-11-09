from django import forms
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

def task_center(request, page):
    all_task_data = Task.objects.all().order_by("task_id")
    all_task_state_data = TaskStateTable.objects.all()
    search_data = {}
    search_data["task_state"] = "全部"
    if request.method =='POST':
        search_filter = {}
        search_data = {}
        task_id = request.POST['task_id']
        task_name = request.POST['task_name']
        state_selection = request.POST['dropdownMenu-value']
        state_selection_num = TaskStateTable.objects.filter(task_state_name = state_selection).first()
        start_time = request.POST['start_time']
        end_time = request.POST['end_time']
        # print(task_id)
        # print(task_name)
        # print(state_selection)
        # print(start_time)
        # print(end_time)
        # 查询
        if task_id:
            search_filter["task_id__contains"] = task_id
            search_data["task_id"] = task_id
        if task_name:
            search_filter["task_name__contains"] = task_name
            search_data["task_name"] = task_name
        if state_selection_num:
            search_filter["task_state"] = state_selection_num 
            search_data["task_state"] = state_selection
        else:
            search_data["task_state"] = "全部"
        if start_time:
            search_filter["task_create_time__gte"] = start_time
            search_data["start_time"] = start_time
        if end_time:
            search_filter["task_create_time__lte"] = end_time
            search_data["end_time"] = end_time
        all_task_data = Task.objects.filter(**search_filter).order_by('task_id')
        print(state_selection_num)
    
    for task in all_task_data:
        task.task_create_time = task.task_create_time.strftime("%Y-%m-%d %H:%M:%S")

    # 实现分页显示
    # 获取传来的page
    # 如果用户未输入page参数，默认为1
    if page == None:
        page = 1
    page_max_item = 5   # 一页最多多少行数据
    start = (page - 1) * page_max_item  # 切片开始位
    end = page * page_max_item  #切片结束位
    total = all_task_data.count()   # 计数
    all_task_data =  all_task_data[start:end]

    # 页码
    page_num = int(total / page_max_item)
    if total % page_max_item:
        page_num += 1

    x = 1
    y = 5
    if page <= x:
        pre_list = range(1, page)
    else:
        pre_list = range(page - x, page)
    
    if page > page_num - y:
        next_list = range(page + 1, page_num + 1)
    else:
        next_list = range(page + 1, page + y + 1)
    if page == 1:
        last_page = 1
        next_page = page + 1
    elif page == page_num:
        last_page = page - 1
        next_page = page_num
    else:
        last_page = page - 1
        next_page = page + 1
    
    print(page)
    print(last_page)
    print(next_page)
    
    return render(request, 'news/task_center.html', 
                  {"task_data": all_task_data, 
                   "task_state_data": all_task_state_data, 
                   "search_data": search_data,
                   "pre_list": pre_list,
                   "next_list": next_list,
                   "last_page": last_page, 
                   "now_page": page,
                   "next_page": next_page})

def home_task_center(request, page):
    # 获取传来的page
    # 如果用户未输入page参数，默认为1
    if page == None:
        page = 1
    print(page)
    return render(request, 'news/home_task_center.html', {"page": page})

'''
class TaskAddForm(forms.ModelForm):
    # 新建任务的ModelForm
    class Meta:
        model = Task
        fields = ["task_id", "task_name", "task_state", "scene", "task_creator", "task_create_time",
                  "product_name", "product_version", "product_description", "product_td" ,"product_ad",
                  "app_ip", "app_domain_name", "app_starting_url", "app_port", "app_name", "app_os_version"]
'''
def task_add(request):
    all_scene_data = Scene.objects.all()
    all_si_data = SafetyIndicator.objects.all()
    if request.method == "POST":
        new_task = Task()
        task_name = request.POST['task_name']
        scene_name = request.POST['dropdownMenu1-value']
        si_category = request.POST['dropdownMenu2-value']
        product_name = request.POST['product_name']
        '''
        new_img = Task(
            product_TD = request.FILES.get('product_TD'),  # 拿到图片
            product_AD = request.FILES.get('product_AD')
        )
        # new_img.save()  # 保存图片'''
        product_version = request.POST['product_version']
        product_description = request.POST['product_description']
        app_IP = request.POST['app_IP']
        app_DN = request.POST['app_DN']
        app_starting_url = request.POST['app_starting_url']
        app_port = request.POST['app_port']
        app_name = request.POST['app_name']
        app_os_version = request.POST['app_os_version']

        new_task.task_id = '66666666'   # TODO 自动创建ID
        new_task.task_name = task_name
        # new_task.task_state = 0   # TODO 连表查询改为id
        # new_task.scene = scene_name # TODO 连表查询改为id
        # new_task.si_category = si_category # TODO 改为可以创建多个安全指标，并且实现连表查询
        new_task.product_name = product_name
        new_task.product_version = product_version
        new_task.product_description = product_description
        new_task.app_ip = app_IP
        new_task.app_domain_name = app_DN
        new_task.app_starting_url = app_starting_url
        new_task.app_port = app_port
        new_task.app_name = app_name
        new_task.app_os_version = app_os_version
        new_task.save()

        print(task_name)
        print(scene_name)
        print(si_category)
        print(product_name)
        print(product_version)
        print(product_description)
        print(app_IP)
        print(app_DN)
        print(app_starting_url)
        print(app_port)
        print(app_name)
        print(app_os_version)

        return redirect('/home/task_center/', page=1)

    return render(request, 'news/task_add.html', {"scene_name_data": all_scene_data, "si_category_data": all_si_data})

def home_task_add(request):
    return render(request, 'news/home_task_add.html')
