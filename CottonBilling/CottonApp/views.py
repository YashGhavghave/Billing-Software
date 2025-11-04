from django.shortcuts import render, redirect
from .models import CottonData, InvoiceSettings
from .forms import  CottonDataForm
from django.db.models import Q
import reportlab
from reportlab.pdfgen import canvas
from django.http import FileResponse
from . import views
import io
from reportlab.lib import pagesizes
from .models import InvoiceSettings
from django.http import HttpResponse


def some_view(request, invoice_id):

    invoice = InvoiceSettings.objects.get(id=invoice_id)


    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="invoice.pdf"'

    buffer= io.BytesIO()
    p= canvas.Canvas(buffer, pagesize= pagesizes.A4)
    p.setTitle(f"{invoice.customer_name}")
    p.setFont("Helvetica", 12)

    x, y = 200, 750
    line_height = 20  # <-- spacing between lines (in points)

    lines = [
        f"Bill Id: {invoice.id}",
        f"Customer Name: {invoice.customer_name}",
        f"Customer Contact: {invoice.customer_number}",
        f"Driver Name: {invoice.driver_name}",
        f"Vehicle Number: {invoice.vehicle_number}",
        f"Ginning Name: {invoice.ginning_name}",
        f"Total Weight: {invoice.total_weight}",
        f"Cotton Weight: {invoice.cotton_weight}",
        f"Market Rate: {invoice.market_rate}",
        f"Bedding Rate: {invoice.bedding_rate}",
        f"Total Amount: {invoice.total_amount}",
        f"Advance Paid: {invoice.advance_paid}",
        f"Balance Amount: Rs. {invoice.balance_amount}",
    ]

    for line in lines:
        p.drawString(x, y, line)
        y -= line_height 

    p.showPage()
    p.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename=('iti.pdf'))


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
        