from django.shortcuts import render
from .models import *
from django.db.models import Q

# Create your views here.
def landing(request):
    return render(request, 'main_app/landing.html')

def main_app(request):
    batteryrange = Batteryrange.objects.all()
    context = {'batteryrange': batteryrange}
    return render(request, 'main_app/index.html', context)

def showcase(request):
    batteryrange = Batteryrange.objects.all()
    context = {'batteryrange': batteryrange}
    return render(request, 'main_app/products.html', context)

def details(request, range ):
    related = Batteryrange.objects.all()
    batteryrange = Batteryrange.objects.filter(range_name=range)
    batterymodel = Batterymodel.objects.filter(range_id__range_name=range)
    applications = Application.objects.filter(range_id__range_name=range)
    context = {'batteryrange': batteryrange, 'batterymodel': batterymodel, 'related': related, 'applications': applications}
    return render(request, 'main_app/details.html', context)


def models(request, model_name):
    batterymodel = Batterymodel.objects.filter(part_number=model_name)
    compatability = Compatability.objects.all()
    bikes = Bikes.objects.filter(model_id=model_name)
    bike_comp = Compatabilitybike.objects.filter(bike_id__model_id=model_name)
    print(batterymodel)
    print(model_name)
    print(bikes)
    print(bike_comp)
    context = {'batterymodel': batterymodel, 'compatability': compatability, 'model_name': model_name, 'bikes': bikes, 'bike_comp': bike_comp}
    return render(request, 'main_app/models.html', context)

def search(request, range, range_name):
    args =range_name
    args2 =range_name
    args3 =range_name
    if request.method == 'POST':
        oem = request.POST.get('search_l')
        oem1 = oem.lower()
        oem2 = oem.capitalize()
        oem3 = oem.capitalize()
        oem1 = oem1.encode('ascii', 'ignore').decode()
        oem1 = oem1.title()
        args = oem1
        args2 = oem2
        args3 = oem3
        range = None
        range_name = "vm"
    brange = Batteryrange.objects.filter(range_name=range)
    bmodel = Batterymodel.objects.filter(range_id__range_name=range)
    batteryrange = Batteryrange.objects.filter(range_name=range_name)
    batterymodel = Batterymodel.objects.filter(range_id__range_name=range_name)
    compatability = Compatability.objects.all().filter(OEM__contains=args)
    bb = Batterymodel.objects.filter(part_number__contains=args2)
    ll = Compatability.objects.filter(vehicle_models__contains=args3)
    bikes = Bikes.objects.filter(model_id__contains=args3)
    bikes_comp = Compatabilitybike.objects.filter(OEM__contains=args3)
    bike_app = Compatabilitybike.objects.filter(application__contains=args3)
    print(args)
    print(args2)
    print(args3)
    print(brange)
    print(bmodel)
    print(batteryrange)
    print(batterymodel)
    print(compatability)
    print(ll)
    print(bb)
    print(bikes)
    print(bikes_comp)
    print(bike_app)

    context = {'batteryrange': batteryrange, 'batterymodel': batterymodel, 'compatability': compatability,'args': args, 'range_name': range_name, 'args2': args2, 'bb': bb, 'll': ll, 'range': range, 'brange': brange, 'bmodel':bmodel, 'bikes': bikes, 'bikes_comp': bikes_comp, 'bike_app': bike_app }
    return render(request, 'main_app/search.html', context)


def search2(request, name):
    args = name
    args2 = name
    type = None
    if request.method == 'POST':
        query = request.POST.get('search_l')
        args = None
        args2 = query.upper()


    series = Amaronmodels.objects.filter(series_id__series__contains=args2)
    usage = Amaronmodels.objects.filter(series_id__usage__contains=args2)
    if args2 == "C10":
        type = Amaronmodels.objects.filter(type__contains=args2)
    print(args)
    print(args2)
    print(series)
    print(usage)
    print(type)
    context = { 'args': args, 'args2': args2, 'series': series, 'usage': usage, 'type': type}

    return render(request, 'main_app/search2.html', context)


def amaron(request):
    return render(request, 'main_app/amaron.html')


def amarondetails(request, amodel):
    aseries = Amaronseries.objects.filter(series=amodel)
    amodel = Amaronmodels.objects.filter(item=amodel)
    context = { 'aseries': aseries, 'amodel': amodel}
    return render(request, 'main_app/amarondetails.html', context)


def about(request):
    return render(request, 'main_app/about.html')

def contacts(request):
    return render(request, 'main_app/contact.html')


