from .models import KUBS_Grains_Data
from django import forms


class GrainsDataForm(forms.ModelForm):
    class Meta:
        model = KUBS_Grains_Data
        fields = [
            'farmers_name',
            'contact_number',
            'driver_name',
            'driver_contact_number',
            'vehicle_number',
            'grain_type',
            'buyer_name',
            'market_rate',
            'bedding_rate',
            'quantity',
            # 'perbag_weight',  # Uncomment if used later
            # 'price_quintal',  # Uncomment if used later
            'advance_amount',
            'total_amount',
            'balance_amount',
            'date_of_transaction',
        ]

        labels = {
            'farmers_name': 'Farmer Name',
            'contact_number': 'Contact Number',
            'driver_name': 'Driver Name',
            'driver_contact_number': 'Driver Contact Number',
            'vehicle_number': 'Vehicle Number',
            'grain_type': 'Type of Grain',
            'buyer_name': 'Buyer Name',
            'market_rate': 'Market Rate (₹ per Quintal)',
            'bedding_rate': 'Bedding Rate (₹ per Quintal)',
            'quantity': 'Total Quantity (kg)',
            'advance_amount': 'Advance Paid (₹)',
            'total_amount': 'Total Amount (₹)',
            'balance_amount': 'Balance Amount (₹)',
            'date_of_transaction': 'Date of Transaction',
        }

        widgets = {
            'farmers_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter farmer name'}),
            'contact_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter contact number'}),
            'driver_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter driver name'}),
            'driver_contact_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter driver contact'}),
            'vehicle_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter vehicle number'}),
            'grain_type': forms.Select(attrs={'class': 'form-select'}),
            'buyer_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter buyer name'}),
            'market_rate': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': 'Market rate ₹/Quintal'}),
            'bedding_rate': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': 'Bedding rate ₹/Quintal'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': 'Total weight in kg'}),
            'advance_amount': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': 'Advance ₹'}),
            'total_amount': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': 'Total amount ₹'}),
            'balance_amount': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': 'Balance ₹'}),
            'date_of_transaction': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),

            'total_amount': forms.NumberInput(attrs={
    'class': 'form-control bg-gray-100',
    'step': '0.01',
    'placeholder': 'Total amount ₹',
    'readonly': 'readonly'
}),
'balance_amount': forms.NumberInput(attrs={
    'class': 'form-control bg-gray-100',
    'step': '0.01',
    'placeholder': 'Balance ₹',
    'readonly': 'readonly'
}),

        }
