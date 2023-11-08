from django.shortcuts import render
from .models import SafetyIndicator
from .forms import IndicatorForm
from datetime import datetime


# Create your views here.
def admin_view(request):
    return render(request, 'admin.html')

def indicators_view(request):
    # if request.method == 'GET':
    #     all_si = SafetyIndicator.objects.all()
    #     return render(request, 'indicators.html', {'si_queryset': all_si})
    if request.method == 'POST':
        if request.POST.get('action') == 'create':
            SafetyIndicator.objects.create(si_id = len(SafetyIndicator.objects.all()) + 1,
                                            si_category = request.POST.get('category'),
                                            si_name = request.POST.get('name'),
                                            si_state = 1,
                                            si_creator = 'admin',
                                            si_create_time = datetime.now())
        if request.POST.get('action') == 'delete':
            SafetyIndicator.objects.filter(si_id = request.POST.get('id')).delete()
        if request.POST.get('action') == 'update':
            SafetyIndicator.objects.filter(si_id = request.POST.get('id')).update(
                si_category = request.POST.get('category'),
                si_name = request.POST.get('name'))
    all_si = SafetyIndicator.objects.all()
    return render(request, 'indicators.html', {'si_queryset': all_si})
        

def scenes_view(request):
    return render(request, 'scenes.html')

def ind_create(request):
    return render(request, "ind_create.html")
    # if request.method == "GET":
    #     form = IndicatorForm()
    #     return render(request, "ind_create.html", {"form": form})
    
def ind_update(request):
    if request.method == "GET":
        si = SafetyIndicator.objects.filter(si_id = request.GET.get('id'))
        return render(request, "ind_update.html", {"si_id": si[0].si_id, "si_category": si[0].si_category, "si_name": si[0].si_name})