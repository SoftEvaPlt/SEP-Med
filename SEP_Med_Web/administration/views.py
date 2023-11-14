from django.shortcuts import render
from django.db.models import Max
from django.core.cache import cache
from .models import SafetyIndicator, Scene
from datetime import datetime,timedelta
import math

def page_div(all, creaiton_flag):
    page_len = 9 #页长

    page_max = math.ceil(all.count() / page_len)
    page = cache.get('page')
    if page == None:
        page = 1
        cache.set('page', 1)
    if creaiton_flag or page > page_max:# 创建新指标后自动跳转最后一页 或搜索后页数变少也跳至最后一页
        page = page_max
    if page != 0:
        all =  all[(page - 1) * page_len : page * page_len] #将指定页码所包含的条目分出来

    print('page:',page)
    pre,next = 2,2
    last_page = page - 1
    next_page = page + 1
    if(last_page == 0):
        last_page = None
    if(next_page == page_max + 1):
        next_page = None
    pages = range(max(page - pre, 1),min(page + next, page_max) + 1)
    return all, pages, last_page, page, next_page

def search(all,class_name):
    if cache.get('ser_1') == None:
        cache.set('ser_1', '')
    if cache.get('ser_2') == None:
        cache.set('ser_2', '')
    if cache.get('ser_3') == None:
        cache.set('ser_3', '')
    if cache.get('ser_4') == None:
        cache.set('ser_4', '全部')
    if cache.get('ser_5') == None:
        cache.set('ser_5', '全部')

    state = ''
    if cache.get('ser_4') == '已启用':
        state = '1'
    if cache.get('ser_4') == '已禁用':
        state = '0'
    if cache.get('ser_5') == '全部':
        if class_name == 'safety_indicator':
            all = all.filter(si_category__contains = cache.get('ser_1'),
                            si_name__contains = cache.get('ser_2'),
                            si_creator__contains = cache.get('ser_3'),
                            si_state__contains = state)
        elif class_name == 'scene':
            all = all.filter(scene_name__contains = cache.get('ser_1'),
                            scene_description__contains = cache.get('ser_2'),
                            scene_creator__contains = cache.get('ser_3'),
                            scene_state__contains = state)

    else:
        time = datetime.now()
        if cache.get('ser_5') == '近一天':
            time -= timedelta(days=1)
        if cache.get('ser_5') == '近一周':
            time -= timedelta(weeks=1)
        if cache.get('ser_5') == '近一月':
            time -= timedelta(days=30)
        if cache.get('ser_5') == '近一年':
            time -= timedelta(days=365)
        if class_name == 'safety_indicator':
            all = all.filter(si_category__contains = cache.get('ser_1'),
                            si_name__contains = cache.get('ser_2'),
                            si_creator__contains = cache.get('ser_3'),
                            si_state__contains = state,
                            si_create_time__gte = time)
        elif class_name == 'scene':
            all = all.filter(scene_name__contains = cache.get('ser_1'),
                            scene_description__contains = cache.get('ser_2'),
                            scene_creator__contains = cache.get('ser_3'),
                            scene_state__contains = state,
                            scene_create_time__gte = time)

    return all

# Create your views here.
def admin_view(request):
    return render(request, 'admin.html')

def indicators_view(request):
    all_si = SafetyIndicator.objects.all()
    if request.method == 'GET':
        if request.GET.get('page') != None:
            cache.set('page', int(request.GET.get('page')))
        else:
            cache.set('page', 1)
            cache.set('ser_1', '')
            cache.set('ser_2', '')
            cache.set('ser_3', '')
            cache.set('ser_4', '全部')
            cache.set('ser_5', '全部')
    if request.POST.get('action') == 'search':
        cache.set('ser_1',request.POST.get('category'))
        cache.set('ser_2',request.POST.get('name'))
        cache.set('ser_3',request.POST.get('creator'))
        cache.set('ser_4',request.POST.get('state'))
        cache.set('ser_5',request.POST.get('time'))

    all_si = search(all_si, 'safety_indicator')
    all_si, pages, last_page, page, next_page = page_div(all_si, 0)
    return render(request, 'indicators.html', {'si_queryset': all_si, 
                                               'create_failed':'False',
                                               'delete_failed':'False',
                                               'pages':pages,
                                               'last_page': last_page,
                                               'now_page': page,
                                               'next_page': next_page})

def ind_create(request):
    if request.method == 'GET':
        return render(request, 'ind_create.html')
    
    if request.method == 'POST':
        if SafetyIndicator.objects.filter(si_name = request.POST.get('name')).exists():
            all_si = SafetyIndicator.objects.all()
            all_si = search(all_si, 'safety_indicator')
            all_si, pages, last_page, page, next_page = page_div(all_si, 0)
            return render(request, 'indicators.html', {'si_queryset': all_si, 
                                                    'create_failed':'True',
                                                    'delete_failed':'False',
                                                    'pages':pages,
                                                    'last_page': last_page,
                                                    'now_page': page,
                                                    'next_page': next_page})
        if len(SafetyIndicator.objects.all()) == 0:
            id = 1
        else:
            id = SafetyIndicator.objects.aggregate(Max('si_id'))['si_id__max'] + 1
        SafetyIndicator.objects.create(si_id = id,
                                        si_category = request.POST.get('category'),
                                        si_name = request.POST.get('name'),
                                        si_state = 1,
                                        si_creator = 'admin',
                                        si_create_time = datetime.now())
        
        all_si = SafetyIndicator.objects.all()
        all_si = search(all_si, 'safety_indicator')
        all_si, pages, last_page, page, next_page = page_div(all_si, 1)
        return render(request, 'indicators.html', {'si_queryset': all_si, 
                                                'create_failed':'False',
                                                'delete_failed':'False',
                                                'pages':pages,
                                                'last_page': last_page,
                                                'now_page': page,
                                                'next_page': next_page})
    
def ind_delete(request):
    if len(SafetyIndicator.objects.all()) == 1 and len(Scene.objects.all()) > 0:
        all_si = SafetyIndicator.objects.all()
        all_si = search(all_si, 'safety_indicator')
        all_si, pages, last_page, page, next_page = page_div(all_si, 0)
        return render(request, 'indicators.html', {'si_queryset': all_si,
                                                    'create_failed':'False',
                                                    'delete_failed':'True',
                                                    'pages':pages,
                                                    'last_page': last_page,
                                                    'now_page': page,
                                                    'next_page': next_page})
    if request.method == 'GET':
        SafetyIndicator.objects.filter(si_id = request.GET.get('id')).delete()

    all_si = SafetyIndicator.objects.all()
    all_si = search(all_si, 'safety_indicator')
    all_si, pages, last_page, page, next_page = page_div(all_si, 0)
    return render(request, 'indicators.html', {'si_queryset': all_si, 
                                            'create_failed':'False',
                                            'delete_failed':'False',
                                            'pages':pages,
                                            'last_page': last_page,
                                            'now_page': page,
                                            'next_page': next_page})
    
def ind_update(request):
    if request.method == 'GET':
        si = SafetyIndicator.objects.filter(si_id = request.GET.get('id'))
        return render(request, 'ind_update.html', {'si_id': si[0].si_id, 
                                                   'si_category': si[0].si_category, 
                                                   'si_name': si[0].si_name})
    
    if request.method == 'POST':
        if SafetyIndicator.objects.filter(si_name = request.POST.get('name')).exists():
            all_si = SafetyIndicator.objects.all()
            all_si = search(all_si, 'safety_indicator')
            all_si, pages, last_page, page, next_page = page_div(all_si, 0)
            return render(request, 'indicators.html', {'si_queryset': all_si, 
                                                    'create_failed':'True',
                                                    'delete_failed':'False',
                                                    'pages':pages,
                                                    'last_page': last_page,
                                                    'now_page': page,
                                                    'next_page': next_page})

        si = SafetyIndicator.objects.get(si_id = request.POST.get('id'))
        si.si_category = request.POST.get('category')
        si.si_name = request.POST.get('name')
        si.save()

        all_si = SafetyIndicator.objects.all()
        all_si = search(all_si, 'safety_indicator')
        all_si, pages, last_page, page, next_page = page_div(all_si, 0)
        return render(request, 'indicators.html', {'si_queryset': all_si, 
                                                'create_failed':'False',
                                                'delete_failed':'False',
                                                'pages':pages,
                                                'last_page': last_page,
                                                'now_page': page,
                                                'next_page': next_page})

def ind_enable(request):
    if request.method == 'GET':
        si = SafetyIndicator.objects.get(si_id = request.GET.get('id'))
        si.si_state = 1
        si.save()

    all_si = SafetyIndicator.objects.all()
    all_si = search(all_si, 'safety_indicator')
    all_si, pages, last_page, page, next_page = page_div(all_si, 0)
    return render(request, 'indicators.html', {'si_queryset': all_si, 
                                               'create_failed':'False',
                                               'delete_failed':'False',
                                               'pages':pages,
                                               'last_page': last_page,
                                               'now_page': page,
                                               'next_page': next_page})
    
def ind_disable(request):
    if request.method == 'GET':
        si = SafetyIndicator.objects.get(si_id = request.GET.get('id'))
        si.si_state = 0
        si.save()

    all_si = SafetyIndicator.objects.all()
    all_si = search(all_si, 'safety_indicator')
    all_si, pages, last_page, page, next_page = page_div(all_si, 0)
    return render(request, 'indicators.html', {'si_queryset': all_si, 
                                               'create_failed':'False',
                                               'delete_failed':'False',
                                               'pages':pages,
                                               'last_page': last_page,
                                               'now_page': page,
                                               'next_page': next_page})



def scenes_view(request):
    all_sc = Scene.objects.all()
    if request.method == 'GET':
        if request.GET.get('page') != None:
            cache.set('page', int(request.GET.get('page')))
        else:
            cache.set('page', 1)
            cache.set('ser_1', '')
            cache.set('ser_2', '')
            cache.set('ser_3', '')
            cache.set('ser_4', '全部')
            cache.set('ser_5', '全部')
    if request.POST.get('action') == 'search':
        cache.set('ser_1',request.POST.get('name'))
        cache.set('ser_2',request.POST.get('description'))
        cache.set('ser_3',request.POST.get('creator'))
        cache.set('ser_4',request.POST.get('state'))
        cache.set('ser_5',request.POST.get('time'))

    all_sc = search(all_sc, 'scene')
    all_sc, pages, last_page, page, next_page = page_div(all_sc, 0)
    return render(request, 'scenes.html', {'sc_queryset': all_sc, 
                                            'create_failed_1':'False',
                                            'create_failed_2':'False',
                                            'pages':pages,
                                            'last_page': last_page,
                                            'now_page': page,
                                            'next_page': next_page})

def sce_create(request):
    if request.method == 'GET':
        return render(request, 'sce_create.html')
    
    if request.method == 'POST':
        if len(SafetyIndicator.objects.all()) == 0:
            all_sc = Scene.objects.all()
            all_sc = search(all_sc, 'scene')
            all_sc, pages, last_page, page, next_page = page_div(all_sc, 0)
            return render(request, 'scenes.html', {'sc_queryset': all_sc, 
                                                    'create_failed_1':'False',
                                                    'create_failed_2':'True',
                                                    'pages':pages,
                                                    'last_page': last_page,
                                                    'now_page': page,
                                                    'next_page': next_page})
        
        if Scene.objects.filter(scene_name = request.POST.get('name')).exists():
            all_sc = Scene.objects.all()
            all_sc = search(all_sc, 'scene')
            all_sc, pages, last_page, page, next_page = page_div(all_sc, 1)
            return render(request, 'scenes.html', {'sc_queryset': all_sc, 
                                                    'create_failed_1':'True',
                                                    'create_failed_2':'False',
                                                    'pages':pages,
                                                    'last_page': last_page,
                                                    'now_page': page,
                                                    'next_page': next_page})
        if len(Scene.objects.all()) == 0:
            id = 1
        else:
            id = Scene.objects.aggregate(Max('scene_id'))['scene_id__max'] + 1
        Scene.objects.create(scene_id = id,
                            scene_name = request.POST.get('name'),
                            scene_state = 1,
                            scene_description = request.POST.get('description'),
                            scene_creator = 'admin',
                            scene_create_time = datetime.now())
        
        all_sc = Scene.objects.all()
        all_sc = search(all_sc, 'scene')
        all_sc, pages, last_page, page, next_page = page_div(all_sc, 1)
        return render(request, 'scenes.html', {'sc_queryset': all_sc, 
                                                'create_failed_1':'False',
                                                'create_failed_2':'False',
                                                'pages':pages,
                                                'last_page': last_page,
                                                'now_page': page,
                                                'next_page': next_page})
    
def sce_delete(request):
    if request.method == 'GET':
        Scene.objects.filter(scene_id = request.GET.get('id')).delete()

    all_sc = Scene.objects.all()
    all_sc = search(all_sc, 'scene')
    all_sc, pages, last_page, page, next_page = page_div(all_sc, 0)
    return render(request, 'scenes.html', {'sc_queryset': all_sc, 
                                            'create_failed_1':'False',
                                            'create_failed_2':'False',
                                            'pages':pages,
                                            'last_page': last_page,
                                            'now_page': page,
                                            'next_page': next_page})
    
def sce_update(request):
    if request.method == 'GET':
        sc = Scene.objects.filter(scene_id = request.GET.get('id'))
        return render(request, 'sce_update.html', {'scene_id': sc[0].scene_id, 
                                                   'scene_name': sc[0].scene_name, 
                                                   'scene_description': sc[0].scene_description})

    if request.method == 'POST':
        if Scene.objects.filter(scene_name = request.POST.get('name')).exists():
            all_sc = Scene.objects.all()
            all_sc = search(all_sc, 'scene')
            all_sc, pages, last_page, page, next_page = page_div(all_sc, 1)
            return render(request, 'scenes.html', {'sc_queryset': all_sc, 
                                                    'create_failed_1':'True',
                                                    'create_failed_2':'False',
                                                    'pages':pages,
                                                    'last_page': last_page,
                                                    'now_page': page,
                                                    'next_page': next_page})

        scene = Scene.objects.get(scene_id = request.POST.get('id'))
        scene.scene_name = request.POST.get('name')
        scene.scene_description = request.POST.get('description')
        scene.save()

    all_sc = Scene.objects.all()
    all_sc = search(all_sc, 'scene')
    all_sc, pages, last_page, page, next_page = page_div(all_sc, 0)
    return render(request, 'scenes.html', {'sc_queryset': all_sc, 
                                            'create_failed_1':'False',
                                            'create_failed_2':'False',
                                            'pages':pages,
                                            'last_page': last_page,
                                            'now_page': page,
                                            'next_page': next_page})

def sce_enable(request):
    if request.method == 'GET':
        scene = Scene.objects.get(scene_id = request.GET.get('id'))
        scene.scene_state = 1
        scene.save()

    all_sc = Scene.objects.all()
    all_sc = search(all_sc, 'scene')
    all_sc, pages, last_page, page, next_page = page_div(all_sc, 0)
    return render(request, 'scenes.html', {'sc_queryset': all_sc, 
                                            'create_failed_1':'False',
                                            'create_failed_2':'False',
                                            'pages':pages,
                                            'last_page': last_page,
                                            'now_page': page,
                                            'next_page': next_page})
    
def sce_disable(request):
    if request.method == 'GET':
        scene = Scene.objects.get(scene_id = request.GET.get('id'))
        scene.scene_state = 0
        scene.save()

    all_sc = Scene.objects.all()
    all_sc = search(all_sc, 'scene')
    all_sc, pages, last_page, page, next_page = page_div(all_sc, 0)
    return render(request, 'scenes.html', {'sc_queryset': all_sc, 
                                            'create_failed_1':'False',
                                            'create_failed_2':'False',
                                            'pages':pages,
                                            'last_page': last_page,
                                            'now_page': page,
                                            'next_page': next_page})