from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Pump_Info, Nozzle_Item, Fuel_Type, Transaction_item
from .serializers import PumpInfoSerializer, NozzleItemSerializer, FuelTypeSerializer, TransactionItemSerializer
from rest_framework import viewsets



class PumpInfoViewSet(viewsets.ModelViewSet):
    queryset = Pump_Info.objects.all()
    serializer_class = PumpInfoSerializer


class NozzleItemViewSet(viewsets.ModelViewSet):
    queryset = Nozzle_Item.objects.all()
    serializer_class = NozzleItemSerializer

    def get_queryset(self):
        queryset = Nozzle_Item.objects.all()
        pump = self.request.query_params.get('pump', None)
        if pump is not None:
            queryset = queryset.filter(pump_id=pump)
        return queryset

class FuelTypeViewSet(viewsets.ModelViewSet):
    queryset = Fuel_Type.objects.all()
    serializer_class = FuelTypeSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction_item.objects.all()
    serializer_class = TransactionItemSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()
