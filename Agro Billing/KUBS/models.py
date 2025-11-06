from django.utils import timezone
from django.db import models

GrainsData_Choices = [
    ('Wheat', 'Wheat'),
    ('Rice', 'Rice'),
    ('Pulses', 'Pulses'),
    ('Maize', 'Maize'),
    ('Tur', 'Tur'),
    ('Soyabean', 'Soyabean'),
    ('Chana', 'Chana'),
]

class KUBS_Grains_Data(models.Model):
    farmers_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    driver_name = models.TextField(blank=True, null=True)
    driver_contact_number = models.CharField(max_length=15, blank=True, null=True)
    vehicle_number = models.CharField(max_length=20, blank=True, null=True)
    grain_type = models.CharField(max_length=20, choices=GrainsData_Choices)
    buyer_name = models.CharField(max_length=100)
    market_rate = models.FloatField()
    bedding_rate = models.FloatField()
    quantity = models.FloatField()
    # perbag_weight = models.FloatField()
    # price_quintal = models.FloatField()
    advance_amount = models.FloatField()
    total_amount = models.FloatField()
    balance_amount = models.FloatField()
    date_of_transaction = models.DateField(default=timezone.now())

    # def save(self, *args, **kwargs):
    #     self.balance_amount = self.total_amount - self.advance_amount
    #     self.total_amount = self.quantity * self.bedding_rate
    #     super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.grain_type}, {self.quantity} units at {self.market_rate} each"