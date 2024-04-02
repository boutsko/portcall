from django.test import TestCase
from .models import ShipOwner, Ship, Port, PortCall, BillOfLading
from .serializers import ShipOwnerSerializer, ShipSerializer, PortSerializer, PortCallSerializer, BillOfLadingSerializer

class SerializerTestCase(TestCase):
    def test_ship_owner_serializer(self):
        ship_owner_data = {'name': 'Example Owner', 'address': '123 Main Street'}
        serializer = ShipOwnerSerializer(data=ship_owner_data)
        self.assertTrue(serializer.is_valid())

    def test_ship_serializer(self):
        ship_owner = ShipOwner.objects.create(name='Test Owner', address='456 Elm Street')
        ship_data = {'imo': '123456', 'name': 'Test Ship', 'ship_owner': ship_owner.id}
        serializer = ShipSerializer(data=ship_data)
        self.assertTrue(serializer.is_valid())

    def test_port_serializer(self):
        port_data = {'imo': '789012', 'name': 'Test Port'}
        serializer = PortSerializer(data=port_data)
        self.assertTrue(serializer.is_valid())

#todo: fix tests
    def _test_port_call_serializer(self):
        port_call_data = {'port_name': 'Test Port', 'arrival_date': '2024-04-02'}
        serializer = PortCallSerializer(data=port_call_data)
        self.assertTrue(serializer.is_valid())

    def _test_bill_of_lading_serializer(self):
        bill_of_lading_data = {'shipper': 'Test Shipper', 'consignee': 'Test Consignee', 'port_of_loading': 'Test Port'}
        serializer = BillOfLadingSerializer(data=bill_of_lading_data)
        self.assertTrue(serializer.is_valid())

