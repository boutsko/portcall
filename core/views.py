from rest_framework import viewsets
from .models import ShipOwner, Ship, Port, PortCall, BillOfLading
from .serializers import (ShipOwnerSerializer,
                          ShipSerializer,
                          PortSerializer,
                          PortCallSerializer,
                          BillOfLadingSerializer)
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from weasyprint import HTML


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

    def generate_pdf(self, request, pk, *args, **kwargs):
        bill_of_lading = BillOfLading.objects.get(id=pk)

        context_data = {
            'port_call': bill_of_lading.port_call,
            'shipper': bill_of_lading.shipper,
            'consignee': bill_of_lading.consignee,
            'receiver': bill_of_lading.receiver,
            'notify_party': bill_of_lading.notify_party,
            'description_of_cargo': bill_of_lading.description_of_cargo,
            'quantity': bill_of_lading.quantity,
            'destination': bill_of_lading.destination,
            'master': bill_of_lading.master,
        }

        template = get_template('bill_of_lading_template.html')
        html_content = template.render(context_data)

        pdf_file = HTML(string=html_content, base_url=request.build_absolute_uri()).write_pdf()

        response = HttpResponse(pdf_file, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="bill_of_lading.pdf"'  
        return response
