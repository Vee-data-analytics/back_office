from rest_framework import serializers
from .models import Transaction_item, Pump_Info, Nozzle_Item, Fuel_Type

# Nested serializer for Pump_Info
class PumpInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pump_Info
        fields = ['id', 'pump_number', 'tank_info']

# Nested serializer for Nozzle_Item
class NozzleItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nozzle_Item
        fields = ['id', 'nozzle_name']

# Nested serializer for Fuel_Type
class FuelTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fuel_Type
        fields = ['id', 'fuel_type','fuel_price']

# Main serializer for Transaction_item
class TransactionItemSerializer(serializers.ModelSerializer):
    pump = PumpInfoSerializer(read_only=True)
    nozzle = NozzleItemSerializer(read_only=True)
    fuel_type = FuelTypeSerializer(read_only=True)

    pump_id = serializers.IntegerField(write_only=True)
    nozzle_id = serializers.IntegerField(write_only=True)
    fuel_type_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Transaction_item
        fields = ['id', 'pump', 'nozzle', 'attendant_name', 'fuel_type', 'volume', 'total_cost', 'timestamp', 'processed', 'pump_id', 'nozzle_id', 'fuel_type_id']

    def create(self, validated_data):
        pump_id = validated_data.pop('pump_id')
        nozzle_id = validated_data.pop('nozzle_id')
        fuel_type_id = validated_data.pop('fuel_type_id')

        validated_data['pump'] = Pump_Info.objects.get(id=pump_id)
        validated_data['nozzle'] = Nozzle_Item.objects.get(id=nozzle_id)
        validated_data['fuel_type'] = Fuel_Type.objects.get(id=fuel_type_id)
        validated_data['processed'] = False

        return super().create(validated_data)
