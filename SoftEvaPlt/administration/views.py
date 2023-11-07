from django.shortcuts import render

# Create your views here.
def admin_view(request):
    return render(request, 'admin.html')

def indicators_view(request):
    return render(request, 'indicators.html')

def scenes_view(request):
    return render(request, 'scenes.html')

def new_indicator(request):
    return render(request, 'new_indicator.html')