from django.urls import path, include
from rest_framework import routers
from .views import ShipOwnerViewSet, ShipViewSet, PortViewSet, PortCallViewSet, BillOfLadingViewSet
from django.urls import path
from .views import GeneratePDFView


router = routers.DefaultRouter()
router.register(r'shipowners', ShipOwnerViewSet)
router.register(r'ships', ShipViewSet)
router.register(r'ports', PortViewSet)
router.register(r'portcalls', PortCallViewSet)
router.register(r'billofladings', BillOfLadingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('generate-pdf/', GeneratePDFView.as_view(), name='generate_pdf'),
    path('generate-pdf/<int:bill_of_lading_id>/', GeneratePDFView.as_view(), name='generate_pdf'),  # Specify URL pattern with bill_of_lading_id
]
