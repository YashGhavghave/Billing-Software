from django.db import models
from django.utils import timezone


# CUSTOMER INFORMATION
class CustomerData(models.Model):
    name = models.CharField("Farmer Name", max_length=100)
    contact_number = models.CharField("Contact Number", max_length=15)
    address = models.TextField("Address", blank=True, null=True)
   
    class Meta:
        verbose_name = "Farmer Data"
        verbose_name_plural = "Farmer Data"

    def __str__(self):
        return self.name


# DRIVER & VEHICLE DETAILS
class DriverData(models.Model):
    driver_name = models.CharField("Driver Name", max_length=50)
    vehicle_number = models.CharField("Vehicle Number", max_length=20)
    mobile_number = models.CharField("Mobile Number", max_length=20)
    vehicle_weight = models.FloatField(" Vehicle Weight (kg)")
    date_of_entry = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "Driver Data"
        verbose_name_plural = "Driver Data"

    def __str__(self):
        return f"{self.vehicle_number} - {self.driver_name}"


# VEHICLE UNLOADING DETAILS 
class VehicleUnloadingData(models.Model):
    driver = models.ForeignKey(
        DriverData,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="unloading_entries"
    )
    loaded_vehicle_weight = models.FloatField("Loaded Vehicle Weight (kg)")
    unloading_vehicle_weight = models.FloatField("Unloading Vehicle Weight (kg)")
    ginning_name = models.CharField("Ginning Name", max_length=100)
    net_weight = models.FloatField("Net Weight (kg)", default=0)
    date_of_unloading = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        self.net_weight = self.loaded_vehicle_weight - self.unloading_vehicle_weight
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Vehicle Unloading Data"
        verbose_name_plural = "Vehicle Unloading Data"

    def __str__(self):
        return f"{self.driver.vehicle_number if self.driver else 'N/A'} - {self.net_weight} kg"


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
    unloading_data = models.OneToOneField(
        VehicleUnloadingData,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="cotton_entry"
    )

    market_rate = models.FloatField("Market Rate (₹ per Quintal)")
    bedding_rate = models.FloatField("Bedding Rate (₹ per Quintal)")
    total_amount = models.FloatField("Total Amount (₹)", default=0)

    advance_paid = models.FloatField("Advance Paid (₹)", default=0)
    balance_amount = models.FloatField("Balance Amount (₹)", default=0)
    is_paid = models.BooleanField("Payment Received (Cash)", default=False)

    date_of_entry = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if self.unloading_data:
            net_weight = self.unloading_data.net_weight
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
