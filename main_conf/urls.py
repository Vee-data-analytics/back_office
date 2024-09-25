
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from app_conf.views import TransactionViewSet


router = DefaultRouter()
router.register(r'transactions', TransactionViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('backoffice/',include('app_conf.urls')),
]
