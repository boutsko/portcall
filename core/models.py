from django.db import models

class ShipOwner(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)

class Ship(models.Model):
    imo = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    ship_owner = models.ForeignKey(ShipOwner, on_delete=models.CASCADE)

class Port(models.Model):
    imo = models.CharField(max_length=20)
    name = models.CharField(max_length=100)

class PortCall(models.Model):
    ship = models.ForeignKey(Ship, on_delete=models.CASCADE)
    port = models.ForeignKey(Port, on_delete=models.CASCADE)

class BillOfLading(models.Model):
    port_call = models.ForeignKey(PortCall, on_delete=models.CASCADE)
    shipper = models.CharField(max_length=100)
    consignee = models.CharField(max_length=100)
    receiver = models.CharField(max_length=100)
    notify_party = models.CharField(max_length=100)
    description_of_cargo = models.TextField()
    quantity = models.IntegerField()
    destination = models.CharField(max_length=100)
    master = models.CharField(max_length=100)
