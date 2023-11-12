import os
from django import forms
from django.conf import settings
from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
# from django.contrib.auth import login
from .models import TaskSi, User  # 导入自定义用户模型
from .models import Task
from .models import Scene
from .models import TaskStateTable
from .models import SafetyIndicator
from .models import Scene
import ipaddress

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
    page_max_item = 7   # 一页最多多少行数据
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
        previous_page = 1
        next_page = page + 1
    elif page == page_num:
        previous_page = page - 1
        next_page = page_num
    else:
        previous_page = page - 1
        next_page = page + 1
    last_page = page_num

    print(page)
    print(previous_page)
    print(next_page)
    
    return render(request, 'news/task_center.html', 
                  {"task_data": all_task_data, 
                   "task_state_data": all_task_state_data, 
                   "search_data": search_data,
                   "pre_list": pre_list,
                   "next_list": next_list,
                   "previous_page": previous_page, 
                   "now_page": page,
                   "next_page": next_page,
                   "first_page": 1,
                   "last_page": last_page})

def home_task_center(request, page):
    # 获取传来的page
    # 如果用户未输入page参数，默认为1
    if page == None:
        page = 1
    print(page)
    return render(request, 'news/home_task_center.html', {"page": page})

def ip_to_int(ip_address):
    try:
        ip_int = int(ipaddress.IPv4Address(ip_address))
        return ip_int
    except ipaddress.AddressValueError:
        # 处理无效的 IP 地址
        return None

def task_add(request):
    all_scene_data = Scene.objects.all()
    all_si_data = SafetyIndicator.objects.all()
    display_si = SafetyIndicator.objects.filter(si_state=1).first()
    if request.method == "POST":
        if 'submit_all' in request.POST:
            try:
                new_task = Task()
                task_name = request.POST.get('task_name')
                scene_name = request.POST.get('dropdownMenu1-value')
                product_name = request.POST.get('product_name')
                '''
                new_img = Task(
                    product_TD = request.FILES.get('product_TD'),  # 拿到图片
                    product_AD = request.FILES.get('product_AD')
                )
                # new_img.save()  # 保存图片'''
                product_version = request.POST.get('product_version')
                product_description = request.POST.get('product_description')
                app_IP = request.POST.get('app_IP')
                app_DN = request.POST.get('app_DN')
                app_starting_url = request.POST.get('app_starting_url')
                app_port = request.POST.get('app_port')
                app_name = request.POST.get('app_name')
                app_os_version = request.POST.get('app_os_version')

                new_task.task_id = Task.objects.latest('task_id').task_id + 1   # 获得最大的id并加一
                new_task.task_name = task_name
                new_task.task_state = TaskStateTable.objects.filter(task_state_name="未开始").first()   # 默认状态是0未开始
                new_task.scene = Scene.objects.filter(scene_name=scene_name).first() # 连表查询改为id
                new_task.task_creator = User.objects.filter(user_name='admin').first()  # TODO 需要传递登录信息
                new_task.product_name = product_name
                if product_version:
                    new_task.product_version = product_version
                if product_description:
                    new_task.product_description = product_description
                if app_IP:
                    new_task.app_ip = ip_to_int(app_IP)
                if app_DN:
                    new_task.app_domain_name = app_DN
                if app_starting_url:
                    new_task.app_starting_url = app_starting_url
                if app_port:
                    new_task.app_port = app_port
                if app_name:
                    new_task.app_name = app_name
                if app_os_version:
                    new_task.app_os_version = app_os_version
                new_task.save()


                print(Task.objects.latest('task_id').task_id + 1)
                print(task_name)
                print(TaskStateTable.objects.filter(task_state_name="未开始").first())
                print(Scene.objects.filter(scene_name=scene_name).first())
                print(scene_name)
                print(product_name)
                print(product_version)
                print(product_description)
                print(app_IP)
                print(ip_to_int(app_IP))
                print(app_DN)
                print(app_starting_url)
                print(app_port)
                print(app_name)
                print(app_os_version)

                # 可以创建多个安全指标，并且实现连表查询，插入多条记录
                si_category = request.POST.get('dropdownMenu2-value')   # 获取多选的字符串
                si_category_list = si_category.split('/')               # 分割获得列表
                # 创建插入多条记录的列表
                new_task_si_list = []
                for si in si_category_list:
                    new_task_si_list.append(TaskSi(
                        task=Task.objects.latest('task_id'),    # 获得最大的id
                        si=SafetyIndicator.objects.filter(si_category=si).first()))
                # 一次插入多条记录
                TaskSi.objects.bulk_create(new_task_si_list)

                return redirect('/upload_image_page/')
            
            except IntegrityError as e:
                # 处理唯一性约束违反的情况
                # 这里你可以根据具体情况选择如何提醒用户，例如弹出警告窗口或在页面上显示警告信息
                error_message = str(e)
                if 'task_name' in error_message:
                    task_error_message = "任务名称已存在，请重新输入任务名称"
                    product_error_message = "产品名称已存在，请重新输入产品名称"
                    return render(request, 'news/task_add.html', {
                        "scene_name_data": all_scene_data,
                        "si_category_data": all_si_data,
                        "display_si": display_si,
                        "task_error_message": task_error_message
                    })
                else:
                    product_error_message = "产品名称已存在，请重新输入产品名称"
                    return render(request, 'news/task_add.html', {
                        "scene_name_data": all_scene_data,
                        "si_category_data": all_si_data,
                        "display_si": display_si,
                        "product_error_message": product_error_message
                    })

    return render(request, 'news/task_add.html', {"scene_name_data": all_scene_data, "si_category_data": all_si_data, "display_si": display_si})

def home_task_add(request):
    return render(request, 'news/home_task_add.html')

def task_del(request):
    task_id = request.GET.get('task_id')
    Task.objects.filter(task_id=task_id).delete()
    TaskStateTable.objects.filter(task=task_id).delete()
    return redirect('/task_center/1/')

def upload_image(request):
    # TODO 增加分别上传两种图片的按钮，优化上传页面，将add的确定改为下一步
    task_id = str(Task.objects.latest('task_id').task_id)
    td_where = ""
    ad_where = ""
    if request.method == 'POST':
        if 'td_image' in request.FILES:
            # 获取一个文件管理器对象
            td_file = request.FILES['td_image']
            # 保存文件
            td_file_name = task_id + 'product_TD' + os.path.splitext(td_file.name)[1]
            # 将要保存的地址和文件名称
            td_where = settings.MEDIA_IMAGE_PATH + td_file_name
            # 分块保存image
            content = td_file.chunks()
            with open(td_where, 'wb') as f:
                for i in content:
                    f.write(i)

        if 'ad_image' in request.FILES:            
            # 获取一个文件管理器对象
            ad_file = request.FILES['ad_image']
            # 保存文件
            ad_file_name = task_id + 'product_AD' + os.path.splitext(ad_file.name)[1]
            # 将要保存的地址和文件名称
            ad_where = settings.MEDIA_IMAGE_PATH + ad_file_name
            # 分块保存image
            content = ad_file.chunks()
            with open(ad_where, 'wb') as f:
                for i in content:
                    f.write(i)

        # 上传文件名称到数据库
        Task.objects.filter(task_id=task_id).update(product_td=td_where, product_ad=ad_where)
    
    return redirect('/task_center/1/')


def upload_image_page(request):
    return render(request, 'news/upload_image.html')

def home_upload_image_page(request):
    return render(request, 'news/home_upload_image.html')
