from django.urls import path, include
from rest_framework import routers
from .views import ShipOwnerViewSet, ShipViewSet, PortViewSet, PortCallViewSet, BillOfLadingViewSet

router = routers.DefaultRouter()
router.register(r'shipowners', ShipOwnerViewSet)
router.register(r'ships', ShipViewSet)
router.register(r'ports', PortViewSet)
router.register(r'portcalls', PortCallViewSet)
router.register(r'billofladings', BillOfLadingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
