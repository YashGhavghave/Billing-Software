from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', views.home, name='home'),
    path('AddGrainsData/', views.AddGrainsData, name='AddGrainsData'),
    path('grains-data-entry/', views.grains_data_entry, name='Kubs_grains_data_entry'),
]
