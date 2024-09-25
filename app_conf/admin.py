from django.contrib import admin
from .models import (
Transaction_item,
Nozzle_Item,
Attendant,
Pump_Info,
Tank_Info,
Fuel_Type
)


# Register your models here.
admin.site.register(Transaction_item)
admin.site.register(Nozzle_Item)
admin.site.register(Attendant)
admin.site.register(Pump_Info)
admin.site.register(Tank_Info)
admin.site.register(Fuel_Type)