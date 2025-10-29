from django.contrib import admin
from . import CustomerData, DriverData, CottonData, VehicleUnloadingData

# Register your models here.
admin.site.register(CustomerData, DriverData, CottonData, VehicleUnloadingData)
# admin.site.register(DriverData)
# admin.site.register(CottonData)
# admin.site.register(VehicleUnloadingData)


admin.site.site_header = "Cotton Billing Admin"
admin.site.site_title = "Cotton Billing Admin Portal"
admin.site.index_title = "Welcome to Cotton Billing Admin Portal"