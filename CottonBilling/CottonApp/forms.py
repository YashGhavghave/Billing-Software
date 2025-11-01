from django.forms import ModelForm
from .models import CottonData, VehicleUnloadingData, DriverData, CustomerData

class CottonDataForm(ModelForm):
    class Meta:
        model = CottonData
        fields = [
            'customer',
            'driver',
            'unloading_data',
            'market_rate',
            'bedding_rate',
            'total_amount',
            'advance_paid',
            'balance_amount',
            'is_paid'
        ]

class VehicleUnloadingDataForm(ModelForm):
    class Meta:
        model= VehicleUnloadingData
        fields= [
            'driver',
            'loaded_vehicle_weight',
            'unloading_vehicle_weight',
            'ginning_name',
            'net_weight',
            'date_of_unloading',
        ]


class DriverDataForm(ModelForm):
    class Meta:
        model = DriverData
        fields= [
            'driver_name',
            'vehicle_number',
            'mobile_number',
            'vehicle_weight',
        ]


class CustomerDataForm(ModelForm):
    class Meta:
        model= CustomerData
        fields= [
            'name',
            'contact_number',
            'address',
        ]