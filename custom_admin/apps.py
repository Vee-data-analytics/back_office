from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig



class CustomAdminConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'custom_admin'


class CustomAdminConfig(AdminConfig):
    default_site = 'custom_admin.admin.CustomAdminSite'
