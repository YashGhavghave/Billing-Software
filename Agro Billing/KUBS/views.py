from django.http import HttpResponse
from django.shortcuts import redirect, render
from . import models
from . import forms
from django.db.models import Q
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
import io
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from .models import KUBS_Grains_Data, GrainInvoiceSettings



#pending home view
def home(request):
    query = request.GET.get('q', '').strip()
    grains_entries = KUBS_Grains_Data.objects.all().order_by('-id')
   
    if query:
        grains_entries = grains_entries.filter(
            Q(farmers_name__icontains=query) |
            Q(driver_name__icontains=query) |
            Q(market_rate__icontains=query) |
            Q(bedding_rate__icontains=query) |
            Q(total_amount__icontains=query) |
            Q(advance_amount__icontains=query) |
            Q(balance_amount__icontains=query)|
            Q(grain_type__icontains=query)|
            Q(buyer_name__icontains=query)|
            Q(quantity__icontains=query)|
            Q(contact_number__icontains=query) |
            # Q(driver_name__icontains=query) |
            Q(vehicle_number__icontains=query) |
            Q(driver__contact_number__icontains=query) 
        )


    invoices = GrainInvoiceSettings.objects.all().order_by('-id')

    context = {
        'invoices': invoices,
        'grains_entries': grains_entries,
        'query': query,
    }
    return render(request, 'KUBS_home.html', context)


    # return render(request, 'KUBS_home.html')




# def grains_data_entry(request):
    if request.method == 'POST':
        farmers_name = request.POST.get('farmers_name')
        contact_number = request.POST.get('contact_number')
        driver_name = request.POST.get('driver_name')
        driver_contact_number = request.POST.get('driver_contact_number')
        vehicle_number = request.POST.get('vehicle_number')
        grain_type = request.POST.get('grain_type')
        buyer_name = request.POST.get('buyer_name')
        quantity = float(request.POST.get('quantity'))
        market_rate = float(request.POST.get('market_rate'))
        bedding_rate = float(request.POST.get('bedding_rate'))
        perbag_weight = float(request.POST.get('perbag_weight'))
        # price_quintal = float(request.POST.get('price_per_unit'))
        advance_amount = float(request.POST.get('advance_amount'))

        total_amount = float(request.POST.get('total_amount'))
        balance_amount = float(request.POST.get('balance_amount'))

        grain_data = models.KUBS_Grains_Data(
            farmers_name=farmers_name,
            contact_number=contact_number,
            driver_name=driver_name,
            driver_contact_number=driver_contact_number,
            vehicle_number=vehicle_number,
            grain_type=grain_type,
            buyer_name=buyer_name,
            quantity=quantity,
            market_rate=market_rate,
            bedding_rate=bedding_rate,
            perbag_weight=perbag_weight,
            # price_quintal=price_quintal,
            advance_amount=advance_amount,
            total_amount=total_amount,
            balance_amount=balance_amount
        )
        grain_data.save()

    return render(request, 'KUBS_grains_data_entry.html')



def AddGrainsData(request):
    if request.method== "POST":
        form= forms.GrainsDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("kubs_home")
    else:
        form = forms.GrainsDataForm()
    return render(request, "add_grains.html", {"form": form})



def GenerateReceipt(request, invoice_id):
    Grains_Data = models.KUBS_Grains_Data.objects.filter(id=invoice_id)

    if not Grains_Data.exists():
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
        'Farmer Name',
        'Farmer Contact',
        'Driver Name',
        'Driver Contact',
        'Vehicle Number',
        'Grain Type',
        'Buyer Name',
        'Market Rate',
        'Bedding Rate',
        'Quantity',
        'Advance Paid',
        'Total Amount',
        'Balance Amount',
    ]]

    for grain in Grains_Data:
        data.append([
            grain.farmers_name,
            grain.contact_number,
            grain.driver_name,
            grain.driver_contact_number,
            grain.vehicle_number,
            grain.grain_type,
            grain.buyer_name,
            str(grain.market_rate),
            str(grain.bedding_rate),
            str(grain.quantity),
            str(grain.total_amount),
            str(grain.advance_amount),
            str(grain.balance_amount),
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

    doc.title=f'Grain Billing Invoice - {Grains_Data.first()}'

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
    response['Content-Disposition'] = 'inline; filename=Grains_bill.pdf'
    return response
