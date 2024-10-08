from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from .models import Pump_Info, Nozzle_Item, Fuel_Type, Transaction_item
from .serializers import PumpInfoSerializer, NozzleItemSerializer,FuelTypeSerializer, TransactionItemSerializer
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework.response import Response
import logging
from .serializers import TransactionItemSerializer


class PumpInfoViewSet(viewsets.ModelViewSet):
    queryset = Pump_Info.objects.all()
    serializer_class = PumpInfoSerializer


class NozzleItemViewSet(viewsets.ModelViewSet):
    queryset = Nozzle_Item.objects.all()
    serializer_class = NozzleItemSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        pump = self.request.query_params.get('pump')
        if pump:
            queryset = queryset.filter(pump_id=pump)
        return queryset


class FuelTypeViewSet(viewsets.ModelViewSet):
    queryset = Fuel_Type.objects.all()
    serializer_class = FuelTypeSerializer





logger = logging.getLogger(__name__)

@method_decorator(csrf_exempt, name='dispatch')
class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction_item.objects.all()
    serializer_class = TransactionItemSerializer

    def create(self, request):
        logger.info(f"Received data: {request.data}")
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            logger.info("Data is valid")
            try:
                instance = self.perform_create(serializer)
                logger.info(f"Transaction created: {instance}")
                headers = self.get_success_headers(serializer.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
            except Exception as e:
                logger.error(f"Error creating transaction: {str(e)}", exc_info=True)
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            logger.error(f"Serializer errors: {serializer.errors}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        return serializer.save()



class UnprocessedTransactionsView(APIView):
    def get(self, request):
        pump_id = request.query_params.get('pump_id')
        if pump_id:
            transactions = Transaction_item.objects.filter(pump_id=pump_id, processed=False)
        else:
            transactions = Transaction_item.objects.filter(processed=False)
        serializer = TransactionItemSerializer(transactions, many=True)
        return Response(serializer.data)
