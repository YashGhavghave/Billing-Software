from django.shortcuts import render, redirect
from .models import CottonData
from .forms import  CottonDataForm
from django.db.models import Q
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, tables, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
import io
from reportlab.lib import pagesizes
from .models import InvoiceSettings
from django.http import HttpResponse
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import inch
from django.http import HttpResponse
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
import io
from datetime import datetime
from .models import CottonData

def GenerateReceipt(request, invoice_id):
    cotton_data = CottonData.objects.filter(id=invoice_id)

    if not cotton_data.exists():
        return HttpResponse("Invoice not found", status=404)

    buffer = io.BytesIO()
    styles = getSampleStyleSheet()
    story = []

    # --- Header Section ---
    title_style = ParagraphStyle(
        'Title',
        fontSize=22,
        textColor=colors.HexColor("#1E3A8A"),
        alignment=1,  # Center
        fontName="Helvetica-Bold",
        spaceAfter=8,
    )
    subtitle_style = ParagraphStyle(
        'Subtitle',
        fontSize=12,
        textColor=colors.HexColor("#4B5563"),
        alignment=1,
        spaceAfter=20,
    )

    story.append(Paragraph("MANDI BILLING SOFTWARE", title_style))
    story.append(Spacer(3, 9))
    story.append(Paragraph("Cotton Billing Invoice", subtitle_style))

    # --- Table Header and Data ---
    data = [[
        'Customer Name',
        'Customer Contact',
        'Driver Name',
        'Vehicle Number',
        'Ginning Name',
        'Total Weight',
        'Cotton Weight',
        'Market Rate',
        'Bedding Rate',
        'Total Amount',
        'Advance Paid',
        'Balance Amount',
    ]]

    for cotton in cotton_data:
        data.append([
            cotton.name,
            cotton.contact_number,
            cotton.driver_name,
            cotton.vehicle_number,
            cotton.ginning_name,
            str(cotton.loaded_vehicle_weight),
            str(cotton.net_weight),
            str(cotton.market_rate),
            str(cotton.bedding_rate),
            str(cotton.total_amount),
            str(cotton.advance_paid),
            str(cotton.balance_amount),
        ])

    # --- Column Widths (your same config) ---
    col_widths = [
        1.6 * inch, 1.6 * inch, 1.6 * inch, 1.2 * inch,
        1.6 * inch, 1.0 * inch, 1.0 * inch, 1.0 * inch,
        1.2 * inch, 1.0 * inch, 1.0 * inch, 1.0 * inch
    ]

    # --- Professional Table Styling ---
    table = Table(data, colWidths=col_widths)
    table.setStyle(TableStyle([
        # Header row
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#2563EB")),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 10),

        # Data rows
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (1, 0), (-1, 1), 9),
        ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.whitesmoke, colors.HexColor("#F9FAFB")]),

        # Borders
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('BOX', (0, 0), (-1, -1), 1, colors.HexColor("#2563EB")),
    ]))

    # --- Page Size Calculation (unchanged) ---
    table_width, table_height = table.wrap(0, 0)
    left_margin = right_margin = 50
    top_margin = bottom_margin = 30
    page_width = table_width + left_margin + right_margin
    page_height = table_height + top_margin + bottom_margin
    min_width, min_height = A4
    page_width = max(page_width, min_width)
    page_height = max(page_height, min_height)

    # --- Document Setup (same as your version) ---
    doc = SimpleDocTemplate(
        buffer,
        pagesize=(page_width, page_height),
        leftMargin=left_margin,
        rightMargin=right_margin,
        topMargin=top_margin,
        bottomMargin=bottom_margin
    )

    doc.title=f'Cotton Billing Invoice - {cotton_data.first().name}'

    # --- Add to PDF ---
    story.append(Spacer(1, 12))
    story.append(table)
    story.append(Spacer(1, 24))

    # --- Footer Section ---
    footer_style = ParagraphStyle(
        'Footer',
        fontSize=9,
        alignment=1,
        textColor=colors.HexColor("#6B7280")
    )
    story.append(Paragraph("Thank you for choosing Mandi Billing Software.", footer_style))
    story.append(Paragraph("support@mandibilling.com | +91 98765 43210", footer_style))

    # --- Build PDF ---
    doc.build(story)
    buffer.seek(0)

    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename=cotton_bill.pdf'
    return response

# Create your views here.
def home(request):
    query = request.GET.get('q', '').strip()
    cotton_entries = CottonData.objects.all().order_by('-id')
   
    if query:
        cotton_entries = cotton_entries.filter(
            Q(customer__name__icontains=query) |
            Q(driver__driver_name__icontains=query) |
            Q(market_rate__icontains=query) |
            Q(bedding_rate__icontains=query) |
            Q(total_amount__icontains=query) |
            Q(advance_paid__icontains=query) |
            Q(balance_amount__icontains=query)|
            Q(name__icontains=query) |
            Q(contact_number__icontains=query) |
            Q(address__icontains=query)|
            Q(driver_name__icontains=query) |
            Q(vehicle_number__icontains=query) |
            Q(mobile_number__icontains=query) |
            # Q(vehicle_weight__icontains=query)|
            Q(driver__driver_name__icontains=query) |
            Q(ginning_name__icontains=query) |
            Q(loaded_vehicle_weight__icontains=query) |
            Q(unloading_vehicle_weight__icontains=query) |
            Q(net_weight__icontains=query)
        )


    invoices = InvoiceSettings.objects.all().order_by('-id')

    context = {
        'invoices': invoices,
        'cotton_entries': cotton_entries,
        'query': query,
    }
    return render(request, 'CottonHome.html', context)


def AddCotton(request):
    if request.method== "POST":
        form = CottonDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = CottonDataForm()
    return render(request, "add_cotton.html", {"form": form})
        