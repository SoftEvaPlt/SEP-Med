from django.shortcuts import render
from .models import SafetyIndicator
from .forms import IndicatorForm
from datetime import datetime


# Create your views here.
def admin_view(request):
    return render(request, 'admin.html')

def indicators_view(request):
    if request.method == 'GET':
        all_si = SafetyIndicator.objects.all()
        return render(request, 'indicators.html', {'si_queryset': all_si})
    if request.method == 'POST':
        if request.POST.get('action') == 'create':
            # print(request.POST)
            SafetyIndicator.objects.create(si_id = len(SafetyIndicator.objects.all()) + 1,
                                            si_category = request.POST.get('si_category'),
                                            si_name = request.POST.get('si_name'),
                                            si_state = 1,
                                            si_creator = 'admin',
                                            si_create_time = datetime.now())
            return render(request, 'admin.html')

def scenes_view(request):
    return render(request, 'scenes.html')

def new_indicator(request):
    if request.method == "GET":
        form = IndicatorForm()
        return render(request, "new_indicator.html", {"form": form})