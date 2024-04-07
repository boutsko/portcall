from django.urls import path, include
from rest_framework import routers
from .views import ShipOwnerViewSet, ShipViewSet, PortViewSet, PortCallViewSet, BillOfLadingViewSet
# from .views import MyPDFView
from django.urls import path
from .views import GeneratePDFView
from .views import generate_example_pdf


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
    # path('pdf/', MyPDFView.as_view(), name='pdf_view'),
    path('example/', generate_example_pdf, name='example_view'),
    path('generate-pdf1/', GeneratePDFView.as_view(), name='generate_pdf1'),
]
