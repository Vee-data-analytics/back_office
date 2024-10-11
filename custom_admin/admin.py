from django.contrib import admin
from django.contrib.admin import AdminSite
from app_conf.models import (
Transaction_item,
Nozzle_Item,
Attendant,
Pump_Info,
Tank_Info,
Fuel_Type,
)





class CustomAdminSite(AdminSite):
    site_header = 'Back Office'
    site_title = 'Back Office'
    index_title = 'Welcome to Your Back-office'
    index_template = 'admin/custom_index.html'

custom_admin_site = CustomAdminSite(name='custom_admin')


# Register your models with the custom admin site


custom_admin_site.register(Transaction_item)
custom_admin_site.register(Nozzle_Item)
custom_admin_site.register(Attendant)
custom_admin_site.register(Pump_Info)
custom_admin_site.register(Tank_Info)
custom_admin_site.register(Fuel_Type)

