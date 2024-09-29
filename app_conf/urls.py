from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app_conf.views import (
    TransactionViewSet,
    PumpInfoViewSet,
    NozzleItemViewSet,
    FuelTypeViewSet)

router = DefaultRouter()
router.register(r'pumps', PumpInfoViewSet, basename='pump')
router.register(r'nozzles', NozzleItemViewSet)
router.register(r'fuel-types', FuelTypeViewSet)
router.register(r'transactions', TransactionViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
