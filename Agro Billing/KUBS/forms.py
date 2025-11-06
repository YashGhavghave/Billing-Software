from .models import KUBS_Grains_Data
from django import forms

class GrainsDataForm(forms.ModelForm):
    class Meta:
        model= KUBS_Grains_Data
        fields = '__all__'