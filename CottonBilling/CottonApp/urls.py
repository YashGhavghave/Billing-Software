from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('addcustomer/', views.AddCustomer, name='Add Customer'),
    path('adddriver/', views.AddDriver, name='Add Driver'),
    path('addcotton/', views.AddCotton, name='Add Cotton'),
    path('vehicleunload/', views.AddVehicleUnload, name='Add Vehicle'),
]
