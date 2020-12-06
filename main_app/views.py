from django.shortcuts import render
from .models import *
from django.db.models import Q

# Create your views here.
def main_app(request):
    batteryrange = Batteryrange.objects.all()
    context = {'batteryrange': batteryrange}
    return render(request, 'main_app/index.html', context)

def showcase(request):
    batteryrange = Batteryrange.objects.all()
    context = {'batteryrange': batteryrange}
    return render(request, 'main_app/products.html', context)

def details(request, range_name):
    related = Batteryrange.objects.all()
    batteryrange = Batteryrange.objects.filter(range_name=range_name)
    batterymodel = Batterymodel.objects.filter(range_id__range_name=range_name)
    applications = Application.objects.filter(range_id__range_name=range_name)
    context = {'batteryrange': batteryrange, 'batterymodel': batterymodel, 'related': related, 'applications': applications}
    return render(request, 'main_app/details.html', context)


def models(request, model_name):
    batterymodel = Batterymodel.objects.filter(part_number=model_name)
    compatability = Compatability.objects.all()
    print(compatability)
    print(model_name)
    context = {'batterymodel': batterymodel, 'compatability': compatability, 'model_name': model_name}
    return render(request, 'main_app/models.html', context)

def search(request, range_name):
    args =range_name
    if request.method == 'POST':
        oem = request.POST.get('search_l')
        oem1 = oem.lower()
        oem2 = oem.capitalize()
        oem1 = oem1.encode('ascii', 'ignore').decode()
        oem1 = oem1.title()
    args = oem1
    args2 = oem2
    print(args2)
    batteryrange = Batteryrange.objects.filter(range_name=range_name)
    batterymodel = Batterymodel.objects.filter(range_id__range_name=range_name)
    compatability = Compatability.objects.all().filter(Q(OEM__icontains=args) | Q(model_id__part_number__icontains=args2)).distinct()
    print(compatability)
    context = {'batteryrange': batteryrange, 'batterymodel': batterymodel, 'compatability': compatability,'args': args, 'range_name': range_name, 'args2': args2 }
    return render(request, 'main_app/search.html', context)


def amaron(request):
    return render(request, 'main_app/shop2.html')


def about(request):
    return render(request, 'main_app/about.html')

def contacts(request):
    return render(request, 'main_app/contact.html')