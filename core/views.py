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

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from .utilities import generate_bill_of_lading_pdf
# from rest_framework.response import Response
# from reportlab.pdfgen import canvas
# from django.http import HttpResponse
# from .models import BillOfLading
#from .serializers import BillOfLadingSerializer

class GeneratePDFView(APIView):
    def get(self, request, *args, **kwargs):
        bill_of_lading_id = kwargs.get('bill_of_lading_id')
        bill_of_lading = get_object_or_404(BillOfLading, id=bill_of_lading_id)

        pdf_response = generate_bill_of_lading_pdf(bill_of_lading)

        return pdf_response

