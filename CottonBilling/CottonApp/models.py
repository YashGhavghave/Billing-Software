from django.db import models
from django.utils import timezone


# CUSTOMER INFORMATION
class CustomerData(models.Model):
    name = models.CharField("Customer Name", max_length=100)
    contact_number = models.CharField("Contact Number", max_length=15)
    address = models.TextField("Address", blank=True, null=True)
   

    def __str__(self):
        return self.name


# DRIVER & VEHICLE DETAILS
class DriverData(models.Model):
    driver_name = models.CharField("Driver Name", max_length=50)
    vehicle_number = models.CharField("Vehicle Number", max_length=20)
    vehicle_weight = models.FloatField("Vehicle Weight (kg)")
    date_of_entry = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.vehicle_number} - {self.driver_name}"


# CENTRAL BILL MODEL (COTTON DATA)
class CottonData(models.Model):
    customer = models.ForeignKey(
        CustomerData,
        on_delete=models.CASCADE,
        related_name="cotton_entries"
    )
    driver = models.ForeignKey(
        DriverData,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="cotton_deliveries"
    )

    # Cotton details
    net_weight = models.FloatField("Net Weight (kg)")
    total_weight = models.FloatField("Gross Weight (kg)")
    vehicle_weight = models.FloatField("Vehicle Weight (kg)")
    market_rate = models.FloatField("Market Rate (₹ per Quintal)")
    bedding_rate = models.FloatField("Bedding Rate (₹ per Quintal)")
    total_amount = models.FloatField("Total Amount (₹)")

    # Simple cash-based fields
    advance_paid = models.FloatField("Advance Paid (₹)", default=0)
    balance_amount = models.FloatField("Balance Amount (₹)", default=0)
    is_paid = models.BooleanField("Payment Received (Cash)", default=False)

    date_of_entry = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Cotton Bill - {self.customer.name} ({self.date_of_entry.strftime('%d-%m-%Y')})"


# VEHICLE UNLOADING DETAILS 
class VehicleUnloadingData(models.Model):
    cotton_entry = models.OneToOneField(
        CottonData,
        on_delete=models.CASCADE,
        related_name="vehicle_unloading"
    )
    ginning_Name = models.CharField("Ginning Name", max_length=100)
    unloading_weight = models.FloatField("Unloading Weight (kg)")
    date_of_unloading = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.cotton_entry.driver.vehicle_number if self.cotton_entry.driver else 'N/A'} - {self.unloading_weight} kg"
