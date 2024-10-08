from .models import Transaction_item,Attendant , Pump_Info, Nozzle_Item, Fuel_Type
from rest_framework import serializers


# Nested serializer for Pump_Info
class PumpInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pump_Info
        fields = ['id', 'pump_number', 'tank_info']


class FuelTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fuel_Type
        fields = ['id','fuel_type','fuel_price']

# Nested serializer for Nozzle_Item
class NozzleItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nozzle_Item
        fields = ['id', 'nozzle_name']

# Nested serializer for Fuel_Type
class TransactionItemSerializer(serializers.ModelSerializer):
    attendant = serializers.PrimaryKeyRelatedField(queryset=Attendant.objects.all(), required=False)
    pump = serializers.PrimaryKeyRelatedField(queryset=Pump_Info.objects.all())
    nozzle = serializers.PrimaryKeyRelatedField(queryset=Nozzle_Item.objects.all())
    fuel_type = serializers.PrimaryKeyRelatedField(queryset=Fuel_Type.objects.all())
    attendant_name = serializers.CharField(source='attendant.name', read_only=True)
    nozzle_name = serializers.CharField(source='nozzle.nozzle_name', read_only=True)
    fuel_type_name = serializers.CharField(source='fuel_type.fuel_type', read_only=True)

    class Meta:
        model = Transaction_item
        fields = ['id', 'pump', 'nozzle', 'nozzle_name', 'fuel_type', 'fuel_type_name', 'volume', 'total_cost', 'attendant', 'attendant_name', 'timestamp']

    def create(self, validated_data):
        try:
            # Get nozzle
            nozzle_id = validated_data.get('nozzle')
            nozzle = Nozzle_Item.objects.get(id=nozzle_id.id)
            validated_data['nozzle'] = nozzle

            # Get pump
            pump_id = validated_data.get('pump')
            pump = Pump_Info.objects.get(id=pump_id.id)
            validated_data['pump'] = pump

            # Get fuel_type
            fuel_type_id = validated_data.get('fuel_type')
            fuel_type = Fuel_Type.objects.get(id=fuel_type_id.id)
            validated_data['fuel_type'] = fuel_type

            # Create the transaction item
            return Transaction_item.objects.create(**validated_data)
        except Nozzle_Item.DoesNotExist:
            raise serializers.ValidationError("Invalid nozzle ID")
        except Pump_Info.DoesNotExist:
            raise serializers.ValidationError("Invalid pump ID")
        except Fuel_Type.DoesNotExist:
            raise serializers.ValidationError("Invalid fuel type ID")
        except Exception as e:
            raise serializers.ValidationError(f"Error creating transaction: {str(e)}")

    def validate(self, data):
        # Add any additional validation logic here
        return data
