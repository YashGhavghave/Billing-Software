from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('addcotton/', views.AddCotton, name='Add Cotton'),
    path('invoice/pdf/<int:invoice_id>/', views.some_view, name='invoice_pdf')
]
