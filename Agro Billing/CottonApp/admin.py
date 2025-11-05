from django.contrib import admin
from .models import CottonData


@admin.register(CottonData)
class CottonDataAdmin(admin.ModelAdmin):
    list_display = (
        'market_rate',
        'bedding_rate',
        'total_amount',
        'advance_paid',
        'balance_amount',
        'is_paid',
        'date_of_entry',
    )

    list_filter = ('is_paid', 'date_of_entry')  

admin.site.site_header = "Cotton Billing Admin"
admin.site.site_title = "Cotton Billing Admin Portal"
admin.site.index_title = "Welcome to Cotton Billing Admin Portal"