from django.contrib import admin
from .models import ShipOwner, Ship, Port, PortCall, BillOfLading
from .serializers import ShipOwnerSerializer, ShipSerializer, PortSerializer, PortCallSerializer, BillOfLadingSerializer

class ShipOwnerAdmin(admin.ModelAdmin):
    pass

class ShipAdmin(admin.ModelAdmin):
    pass

class PortAdmin(admin.ModelAdmin):
    pass

class PortCallAdmin(admin.ModelAdmin):
    pass

class BillOfLadingAdmin(admin.ModelAdmin):
    pass

admin.site.register(ShipOwner, ShipOwnerAdmin)
admin.site.register(Ship, ShipAdmin)
admin.site.register(Port, PortAdmin)
admin.site.register(PortCall, PortCallAdmin)
admin.site.register(BillOfLading, BillOfLadingAdmin)
