
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from app_conf.views import TransactionViewSet
from custom_admin.admin import CustomAdminSite
from django.conf import settings
from django.conf.urls.static import static
from custom_admin.admin import custom_admin_site
from django.shortcuts import redirect

router = DefaultRouter()
router.register(r'transactions', TransactionViewSet)

def redirect_to_admin(request):
    return redirect('admin:index')

urlpatterns = [
    path('', redirect_to_admin, name='root'),
    path('admin/', custom_admin_site.urls),
    #path('admin/', admin.site.urls),
    path('backoffice/',include('app_conf.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
 + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
