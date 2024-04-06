from django.http import HttpResponse
from reportlab.pdfgen import canvas

def generate_bill_of_lading_pdf(bill_of_lading_data):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="bill_of_lading_{bill_of_lading_data.id}.pdf"'

    # Create a PDF document using ReportLab canvas
    p = canvas.Canvas(response)
    p.drawString(100, 750, f"Bill of Lading ID: {bill_of_lading_data.id}")

    # Define the fields you want to extract from the BillOfLading object
    fields_to_extract = ['shipper', 'consignee', 'receiver', 'notify_party',
                         'description_of_cargo', 'quantity', 'destination',
                         'master', 'port_call']

    y_position = 700  # Initial Y position for drawing text

    for field_name in fields_to_extract:
        field_value = getattr(bill_of_lading_data, field_name, None)
        if field_value is not None:
            text = f"{field_name.capitalize()}: {field_value}"
            p.drawString(100, y_position, text)
            y_position -= 20  # Move down for the next line

    p.showPage()
    p.save()

    return response

