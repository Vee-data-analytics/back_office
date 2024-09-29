from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Fuel_Type(models.Model):
    FUEL_CHOICES = [
        ('DIESEL', 'Diesel'),
        ('UNLEADED_95', 'Unleaded 95'),
        ('UNLEADED_98', 'Unleaded 98'),
    ]

    fuel_type = models.CharField(max_length=20, choices=FUEL_CHOICES, unique=True)
    fuel_price = models.FloatField()


    def __str__(self):
        return dict(self.FUEL_CHOICES)[self.fuel_type]

class Tank_Info(models.Model):
    tank_number = models.CharField(_("Tank"), max_length=10, unique=True)
    fuel_type = models.ForeignKey(Fuel_Type, on_delete=models.CASCADE)
    capacity = models.FloatField()
    current_volume = models.FloatField()

    def __str__(self):
        return self.tank_number

class Pump_Info(models.Model):
    pump_number = models.IntegerField(_("Pump"), unique=True)
    tank_info = models.ForeignKey(Tank_Info, on_delete=models.CASCADE)

    def __str__(self):
        return f"Pump {self.pump_number}"

class Attendant(models.Model):
    name = models.CharField(_("Attendant Name"), max_length=100, null=True)
    attendant_id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.name or f"Attendant {self.attendant_id}"

class Nozzle_Item(models.Model):
    pump = models.ForeignKey(Pump_Info, on_delete=models.CASCADE, related_name="nozzles")
    attendant = models.ForeignKey(Attendant, on_delete=models.SET_NULL, null=True)
    nozzle_name = models.IntegerField(_("Nozzle"), unique=True, null=True)
    fuel_type = models.ForeignKey(Fuel_Type, on_delete=models.SET_NULL, null=True)
    processed = models.BooleanField(default=False)
    liters = models.FloatField(null=True)
    current_transaction = models.CharField(_("Current Transaction"), max_length=100, null=True)
    last_transaction = models.CharField(_("Last Transaction"), max_length=100, null=True)
    total_unprocessed = models.CharField(_("Total Unprocessed"), max_length=100, null=True)

    def __str__(self):
        return f"Nozzle {self.nozzle_name} at Pump {self.pump.pump_number}"


class Transaction_item(models.Model):
    pump = models.ForeignKey('Pump_Info', on_delete=models.CASCADE)
    nozzle = models.ForeignKey('Nozzle_Item', on_delete=models.CASCADE)
    attendant = models.ForeignKey('Attendant', on_delete=models.SET_NULL, null=True, blank=True)
    fuel_type = models.ForeignKey('Fuel_Type', on_delete=models.CASCADE)
    volume = models.FloatField()
    total_cost = models.FloatField()
    last_transaction = models.CharField(_("Last Transaction"), max_length=100, null=True)
    timestamp = models.DateTimeField(default=timezone.now)
    processed = models.BooleanField(default=False)  # Ensure this field is defined

    def __str__(self):
        attendant = self.attendant.name if self.attendant else "Unknown Attendant"
        return f"Transaction {self.id} at Pump {self.pump.pump_number} - {self.volume} liters - by {attendant}"
