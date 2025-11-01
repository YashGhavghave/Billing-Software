from django.shortcuts import render, redirect
from .models import CustomerData, DriverData, CottonData, VehicleUnloadingData
from .forms import CustomerDataForm, DriverDataForm, CottonDataForm, VehicleUnloadingDataForm

# Create your views here.
def home(request):
    customers = CustomerData.objects.all().order_by('-id')
    drivers = DriverData.objects.all().order_by('-id')
    cotton_entries = CottonData.objects.all().order_by('-id')
    unloading_entries = VehicleUnloadingData.objects.all().order_by('-id')

    return render(request, 'CottonHome.html', {
        'customers': customers,
        'drivers': drivers,
        'cotton_entries': cotton_entries,
        'unloading_entries': unloading_entries,
    })

def AddCustomer(request):
    if request.method== "POST":
        form = CustomerDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = CustomerDataForm()
    return render(request, "add_customer.html", {"form": form})
        

def AddDriver(request):
    if request.method== "POST":
        form = DriverDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = DriverDataForm()
    return render(request, "add_driver.html", {"form": form})
        

def AddCotton(request):
    if request.method== "POST":
        form = CottonDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = CottonDataForm()
    return render(request, "add_cotton.html", {"form": form})
        

def AddVehicleUnload(request):
    if request.method== "POST":
        form = VehicleUnloadingDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = VehicleUnloadingDataForm()
    return render(request, "add_vehicle_unloading.html", {"form": form})

