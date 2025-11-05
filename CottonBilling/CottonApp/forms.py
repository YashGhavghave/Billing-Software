from django.forms import ModelForm
from .models import CottonData
from django import forms

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
        widgets = {
            'loaded_vehicle_weight': forms.NumberInput(attrs={'id': 'loaded_vehicle_weight'}),
            'unloading_vehicle_weight': forms.NumberInput(attrs={'id': 'unloading_vehicle_weight'}),
            'bedding_rate': forms.NumberInput(attrs={'id': 'bedding_rate'}),
            'advance_paid': forms.NumberInput(attrs={'id': 'advance_paid'}),
            
            # Computed (read-only) fields
            'net_weight': forms.NumberInput(attrs={
                'id': 'net_weight', 
                'readonly': True,
                'class': 'bg-gray-100 cursor-not-allowed'
            }),
            'total_amount': forms.NumberInput(attrs={
                'id': 'total_amount', 
                'readonly': True,
                'class': 'bg-gray-100 cursor-not-allowed'
            }),
            'balance_amount': forms.NumberInput(attrs={
                'id': 'balance_amount', 
                'readonly': True,
                'class': 'bg-gray-100 cursor-not-allowed'
            }),
        }

