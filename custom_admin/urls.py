from .views import custom_admin


from django.urls import path
from .views import custom_admin_dashboard
from .admin import custom_admin_site

urlpatterns = [
    path('', custom_admin_dashboard, name='custom_admin_dashboard'),
    path('', custom_admin_site.urls),
]
