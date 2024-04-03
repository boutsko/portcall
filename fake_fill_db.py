import random
from faker import Faker
from django.db import transaction
from core.models import ShipOwner, Ship, Port, PortCall, BillOfLading

fake = Faker()

@transaction.atomic
def populate_database(num_records):
    for _ in range(num_records):
        ship_owner = ShipOwner.objects.create(name=fake.name(), address=fake.address())
        ship = Ship.objects.create(imo=fake.random_int(min=100000, max=999999), name=fake.company(), ship_owner=ship_owner)
        port = Port.objects.create(imo=fake.random_int(min=100000, max=999999), name=fake.city())
        port_call = PortCall.objects.create(ship=ship, port=port)
        BillOfLading.objects.create(
            port_call=port_call,
            shipper=fake.company(),
            consignee=fake.company(),
            receiver=fake.name(),
            notify_party=fake.name(),
            description_of_cargo=fake.text(),
            quantity=random.randint(1, 100),
            destination=fake.city(),
            master=fake.name()
        )

# if __name__ == '__main__':
num_records = 10  # Number of records to create for each model
populate_database(num_records)
