from django.shortcuts import redirect, render
from . import models
from . import forms

def home(request):
    return render(request, 'KUBS_home.html')

def grains_data_entry(request):
    if request.method == 'POST':
        farmers_name = request.POST.get('farmers_name')
        contact_number = request.POST.get('contact_number')
        driver_name = request.POST.get('driver_name')
        driver_contact_number = request.POST.get('driver_contact_number')
        vehicle_number = request.POST.get('vehicle_number')
        grain_type = request.POST.get('grain_type')
        buyer_name = request.POST.get('buyer_name')
        quantity = float(request.POST.get('quantity'))
        market_rate = float(request.POST.get('market_rate'))
        bedding_rate = float(request.POST.get('bedding_rate'))
        perbag_weight = float(request.POST.get('perbag_weight'))
        # price_quintal = float(request.POST.get('price_per_unit'))
        advance_amount = float(request.POST.get('advance_amount'))

        total_amount = float(request.POST.get('total_amount'))
        balance_amount = float(request.POST.get('balance_amount'))

        grain_data = models.KUBS_Grains_Data(
            farmers_name=farmers_name,
            contact_number=contact_number,
            driver_name=driver_name,
            driver_contact_number=driver_contact_number,
            vehicle_number=vehicle_number,
            grain_type=grain_type,
            buyer_name=buyer_name,
            quantity=quantity,
            market_rate=market_rate,
            bedding_rate=bedding_rate,
            perbag_weight=perbag_weight,
            # price_quintal=price_quintal,
            advance_amount=advance_amount,
            total_amount=total_amount,
            balance_amount=balance_amount
        )
        grain_data.save()

    return render(request, 'KUBS_grains_data_entry.html')



def AddGrainsData(request):
    if request.method== "POST":
        form= forms.GrainsDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/home")
    else:
        form = forms.GrainsDataForm()
    return render(request, "add_grains.html", {"form": form})