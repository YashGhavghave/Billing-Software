from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', views.home, name='kubs_home'),
    path('AddGrainsData/', views.AddGrainsData, name='AddGrainsData'),
    path('invoice/pdf/<int:invoice_id>/', views.GenerateReceipt, name='GenerateReceipt')
]
