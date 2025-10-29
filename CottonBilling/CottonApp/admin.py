from django.contrib import admin
from .models import CustomerData
from .models import DriverData
from .models import CottonData
from .models import VehicleUnloadingData

# Register your models here.
# admin.site.register(CustomerData)
# admin.site.register(DriverData)
# admin.site.register(CottonData)
# admin.site.register(VehicleUnloadingData)


@admin.register(CustomerData)
class CustomerDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_number', 'address')
    search_fields = ('name', 'contact_number')


@admin.register(VehicleUnloadingData)
class VehicleUnloadingDataAdmin(admin.ModelAdmin):  
    list_display = ('driver', 'loaded_vehicle_weight', 'unloading_vehicle_weight', 'net_weight', 'ginning_name', 'date_of_unloading')
    search_fields = ('driver__driver_name', 'ginning_name')


@admin.register(DriverData)
class DriverDataAdmin(admin.ModelAdmin):
    list_display = ('driver_name', 'vehicle_number', 'mobile_number', 'vehicle_weight', 'date_of_entry')
    search_fields = ('driver_name', 'vehicle_number', 'mobile_number')


@admin.register(CottonData)
class CottonDataAdmin(admin.ModelAdmin):
    list_display = (
        'customer',
        'driver',
        'unloading_data',
        'market_rate',
        'bedding_rate',
        'total_amount',
        'advance_paid',
        'balance_amount',
        'is_paid',
        'date_of_entry',
    )
    search_fields = ('customer__name', 'driver__driver_name', 'unloading_data__ginning_name')
    list_filter = ('is_paid', 'date_of_entry')  

admin.site.site_header = "Cotton Billing Admin"
admin.site.site_title = "Cotton Billing Admin Portal"
admin.site.index_title = "Welcome to Cotton Billing Admin Portal"