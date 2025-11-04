from django.forms import ModelForm
from .models import CottonData

class CottonDataForm(ModelForm):
    class Meta:
        model = CottonData
        fields = [
            'name',
            'contact_number',
            'address',
            'driver_name',
            'vehicle_number',
            'mobile_number',
            # 'vehicle_weight',
            'market_rate',
            'bedding_rate',
            'total_amount',
            'advance_paid',
            'balance_amount',
            'is_paid',
            'loaded_vehicle_weight',
            'unloading_vehicle_weight',
            'ginning_name',
            'net_weight',
            'date_of_unloading',
        ]
