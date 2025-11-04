from django.db import models
from django.forms import ModelForm
from django.utils import timezone


# CENTRAL BILL MODEL (COTTON DATA)
class CottonData(models.Model):
    # CUSTOMER INFORMATION
    name = models.CharField("Farmer Name", max_length=100)
    contact_number = models.CharField("Contact Number", max_length=15)
    address = models.TextField("Address", blank=True, null=True)
    driver_name = models.CharField("Driver Name", max_length=50)
    vehicle_number = models.CharField("Vehicle Number", max_length=20)
    mobile_number = models.CharField("Mobile Number", max_length=20)
    date_of_entry = models.DateTimeField(default=timezone.now)
    loaded_vehicle_weight = models.FloatField("Loaded Vehicle Weight (kg)")
    unloading_vehicle_weight = models.FloatField("Unloading Vehicle Weight (kg)")
    ginning_name = models.CharField("Ginning Name", max_length=100)
    net_weight = models.FloatField("Net Weight (kg)", default=0)
    date_of_unloading = models.DateTimeField(default=timezone.now)
    market_rate = models.FloatField("Market Rate (₹ per Quintal)")
    bedding_rate = models.FloatField("Bedding Rate (₹ per Quintal)")
    total_amount = models.FloatField("Total Amount (₹)", default=0)
    advance_paid = models.FloatField("Advance Paid (₹)", default=0)
    balance_amount = models.FloatField("Balance Amount (₹)", default=0)
    is_paid = models.BooleanField("Payment Received (Cash)", default=False)

    def save(self, *args, **kwargs):
        self.net_weight = self.loaded_vehicle_weight - self.unloading_vehicle_weight
        if self.unloading_vehicle_weight:
            net_weight = self.unloading_vehicle_weight - self.loaded_vehicle_weight
            self.total_amount = (net_weight / 100) * self.bedding_rate
        else:
            self.total_amount = 0

        self.balance_amount = self.total_amount - self.advance_paid
        self.is_paid = self.balance_amount <= 0

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Cotton Data"
        verbose_name_plural = "Cotton Data"

    def __str__(self):
        return f"Cotton Bill - {self.customer.name} ({self.date_of_entry.strftime('%d-%m-%Y')})"


class InvoiceSettings(models.Model):
    invoice_number = models.CharField("Invoice Number", max_length=20)
    customer_name = models.CharField("Customer Name", max_length=100)
    customer_number = models.CharField("Customer Contact Number", max_length=15)
    driver_name = models.CharField("Driver Name", max_length=50)
    vehicle_number = models.CharField("Vehicle Number", max_length=20)
    ginning_name = models.CharField("Ginning Name", max_length=100)
    total_weight = models.FloatField("Total Weight (kg)")
    cotton_weight = models.FloatField("Cotton Weight (kg)")
    market_rate = models.FloatField("Market Rate (₹ per Quintal)")
    bedding_rate = models.FloatField("Bedding Rate (₹ per Quintal)")
    total_amount = models.FloatField("Total Amount (₹)")
    advance_paid = models.FloatField("Advance Paid (₹)")
    balance_amount = models.FloatField("Balance Amount (₹)")

    def __str__(self):
        return f"Invoice Settings - {self.invoice_number} - {self.customer_name}"


