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


from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from reportlab.pdfgen import canvas
from io import BytesIO
from .utilities import generate_bill_of_lading_pdf

class MyPDFView(View):
    def get(self, request, *args, **kwargs):
        # Get context data to pass to the template
        context = {'foo': 'bar'}

        # Render the HTML template with context data
        template = get_template('my_template.html')
        html_content = template.render(context)

        # Create PDF document using ReportLab
        pdf_buffer = BytesIO()
        p = canvas.Canvas(pdf_buffer)
        p.drawString(100, 750, "My PDF Document")

        # Add HTML content to PDF
        p.drawString(100, 700, html_content)

        p.showPage()
        p.save()

        # Prepare HTTP response with PDF content
        pdf_buffer.seek(0)
        response = HttpResponse(pdf_buffer, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="my_pdf_document.pdf"'
        return response


# from django.shortcuts import render

# def example_view(request):
#     context = {'foo': 'bar'}
#     return render(request, 'example_template.html', context)



from django.http import HttpResponse
from django.template.loader import get_template
from django.conf import settings
from weasyprint import HTML

def generate_example_pdf(request):
    # Get data or context to pass to the template
    context = {'foo': 'bar'}

    # Render the HTML template with context data
    template = get_template('example_template.html')
    html_content = template.render(context)

    # Generate PDF using WeasyPrint
    pdf_file = HTML(string=html_content, base_url=request.build_absolute_uri()).write_pdf()

    # Create HTTP response with PDF content
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'filename="output.pdf"'
    return response
