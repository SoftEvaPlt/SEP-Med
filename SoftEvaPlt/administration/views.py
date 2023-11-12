from django.shortcuts import render
from django.db.models import Max
from .models import SafetyIndicator, Scene
from datetime import datetime
import math


# Create your views here.
def admin_view(request):
    return render(request, 'admin.html')

def indicators_view(request):
    if request.method == 'POST':

        if request.POST.get('action') == 'create':
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
            
        if request.POST.get('action') == 'delete':
            if len(SafetyIndicator.objects.all()) == 1 & len(Scene.objects.all()) > 0:
                return render(request, 'indicators.html', {'si_queryset': SafetyIndicator.objects.all(),
                                                            'delete_failed':'True'})
            SafetyIndicator.objects.filter(si_id = request.POST.get('id')).delete()

        if request.POST.get('action') == 'update':
            SafetyIndicator.objects.filter(si_id = request.POST.get('id')).update(
                si_category = request.POST.get('category'),
                si_name = request.POST.get('name'))
            
        if request.POST.get('action') == 'enable':
            SafetyIndicator.objects.filter(si_id = request.POST.get('id')).update(
                si_state = 1
            )

        if request.POST.get('action') == 'disable':
            SafetyIndicator.objects.filter(si_id = request.POST.get('id')).update(
                si_state = 0
            )

    page_len = 4 #页长
    all_si = SafetyIndicator.objects.all()
    total = all_si.count()
    page = request.GET.get('page')
    if page == None:
        page = 1
    else:
        page = int(page)
    all_si =  all_si[(page - 1) * page_len : page * page_len] #将指定页码所包含的条目分出来

    pre,next = 2,2
    page_max = math.ceil(total / page_len)
    last_page = page - 1
    next_page = page + 1
    if(last_page == 0):
        last_page = None
    if(next_page == page_max + 1):
        next_page = None
    pages = range(max(page - pre, 1),min(page + next, page_max) + 1)

    return render(request, 'indicators.html', {'si_queryset': all_si, 
                                               'delete_failed':'False',
                                               "pages":pages,
                                               "last_page": last_page,
                                               "now_page": page,
                                               "next_page": next_page})

def ind_create(request):
    return render(request, "ind_create.html")
    
def ind_update(request):
    if request.method == "GET":
        si = SafetyIndicator.objects.filter(si_id = request.GET.get('id'))
        return render(request, "ind_update.html", {"si_id": si[0].si_id, 
                                                   "si_category": si[0].si_category, 
                                                   "si_name": si[0].si_name})
    

def scenes_view(request):
    all_sc = Scene.objects.all()
    if request.method == 'POST':

        if request.POST.get('action') == 'create':
            if len(SafetyIndicator.objects.all()) == 0:
                return render(request, 'scenes.html', {'sc_queryset': all_sc, 'create_failed':'True'})
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
            
        if request.POST.get('action') == 'delete':
            Scene.objects.filter(scene_id = request.POST.get('id')).delete()

        if request.POST.get('action') == 'update':
            Scene.objects.filter(scene_id = request.POST.get('id')).update(
                scene_name = request.POST.get('name'),
                scene_description = request.POST.get('description'))
            
        if request.POST.get('action') == 'enable':
            Scene.objects.filter(scene_id = request.POST.get('id')).update(
                scene_state = 1
            )

        if request.POST.get('action') == 'disable':
            Scene.objects.filter(scene_id = request.POST.get('id')).update(
                scene_state = 0
            )

    return render(request, 'scenes.html', {'sc_queryset': all_sc, 'create_failed':'False'})

def sce_create(request):
    return render(request, "sce_create.html")
    
def sce_update(request):
    if request.method == "GET":
        sc = Scene.objects.filter(scene_id = request.GET.get('id'))
        return render(request, "sce_update.html", {"scene_id": sc[0].scene_id, 
                                                   "scene_name": sc[0].scene_name, 
                                                   "scene_description": sc[0].scene_description})
    

def test(request):
    return render(request, 'test.html')