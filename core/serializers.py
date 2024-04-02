from rest_framework import serializers
from .models import ShipOwner, Ship, Port, PortCall, BillOfLading

class ShipOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShipOwner
        fields = '__all__'

class ShipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ship
        fields = '__all__'

class PortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Port
        fields = '__all__'

class PortCallSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortCall
        fields = '__all__'

class BillOfLadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillOfLading
        fields = '__all__'
