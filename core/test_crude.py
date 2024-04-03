from django.test import TestCase
from .models import ShipOwner, Ship, Port, PortCall, BillOfLading

class ModelCRUDTestCase(TestCase):
    def setUp(self):
        self.ship_owner = ShipOwner.objects.create(name='Owner 1', address='123 Main Street')
        self.ship = Ship.objects.create(imo='123456', name='Ship 1', ship_owner=self.ship_owner)
        self.port = Port.objects.create(imo='789012', name='Port 1')
        self.port_call = PortCall.objects.create(ship=self.ship, port=self.port)
        self.bill_of_lading = BillOfLading.objects.create(port_call=self.port_call, shipper='Shipper 1', consignee='Consignee 1', receiver='Receiver 1', notify_party='Notify Party 1', description_of_cargo='Cargo description', quantity=10, destination='Destination 1', master='Master 1')

    def test_create_ship_owner(self):
        new_owner = ShipOwner.objects.create(name='New Owner', address='456 Elm Street')
        self.assertEqual(new_owner.name, 'New Owner')

    def test_read_ship(self):
        ship = Ship.objects.get(imo='123456')
        self.assertEqual(ship.name, 'Ship 1')

    def test_update_port(self):
        port = Port.objects.get(imo='789012')
        port.name = 'Updated Port'
        port.save()
        updated_port = Port.objects.get(imo='789012')
        self.assertEqual(updated_port.name, 'Updated Port')

    def test_delete_bill_of_lading(self):
        bill_of_lading = BillOfLading.objects.get(shipper='Shipper 1')
        bill_of_lading.delete()
        with self.assertRaises(BillOfLading.DoesNotExist):
            BillOfLading.objects.get(shipper='Shipper 1')

    def test_create_port_call(self):
        new_port_call = PortCall.objects.create(ship=self.ship, port=self.port)
        self.assertEqual(new_port_call.ship.imo, '123456')
        self.assertEqual(new_port_call.port.imo, '789012')

    def test_read_port_call(self):
        port_call = PortCall.objects.get(ship__imo='123456')
        self.assertEqual(port_call.port.name, 'Port 1')

    def test_update_port_call(self):
        port_call = PortCall.objects.get(ship__imo='123456')
        port_call.port.name = 'Updated Port'
        port_call.port.save()
        updated_port_call = PortCall.objects.get(ship__imo='123456')
        self.assertEqual(updated_port_call.port.name, 'Updated Port')

    def test_delete_port_call(self):
        port_call = PortCall.objects.get(ship__imo='123456')
        port_call.delete()
        with self.assertRaises(PortCall.DoesNotExist):
            PortCall.objects.get(ship__imo='123456')
