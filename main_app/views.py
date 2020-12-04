from django.shortcuts import render
from .models import *

# Create your views here.
def main_app(request):
    return render(request, 'main_app/index.html')

def showcase(request):
    batterymodels = Batterymodel.objects.all()
    context = {'batterymodels': batterymodels}
    return render(request, 'main_app/products.html', context)

def details(request):
    return render(request, 'main_app/details.html')

def contacts(request):
    return render(request, 'main_app/contact.html')