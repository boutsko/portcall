from rest_framework import viewsets
from .models import ShipOwner, Ship, Port, PortCall, BillOfLading
from .serializers import ShipOwnerSerializer, ShipSerializer, PortSerializer, PortCallSerializer, BillOfLadingSerializer

class ShipOwnerViewSet(viewsets.ModelViewSet):
    queryset = ShipOwner.objects.all()
    serializer_class = ShipOwnerSerializer

class ShipViewSet(viewsets.ModelViewSet):
    queryset = Ship.objects.all()
    serializer_class = ShipSerializer

class PortViewSet(viewsets.ModelViewSet):
    queryset = Port.objects.all()
    serializer_class = PortSerializer

class PortCallViewSet(viewsets.ModelViewSet):
    queryset = PortCall.objects.all()
    serializer_class = PortCallSerializer

class BillOfLadingViewSet(viewsets.ModelViewSet):
    queryset = BillOfLading.objects.all()
    serializer_class = BillOfLadingSerializer

