from django.shortcuts import render
import qrcode
from PIL import Image
from io import BytesIO
import base64
from .forms import ScanForm


def index(request):
    context = {}
    # if request.method == "POST":
    #     qr_text = request.POST.get("qr_text", "")
    #     qr_image = qrcode.make(qr_text, box_size=2)
    #     qr_image_pil = qr_image.get_image()
    #     stream = BytesIO()
    #     qr_image_pil.save(stream, format='PNG')
    #     qr_image_data = stream.getvalue()
    #     qr_image_base64 = base64.b64encode(qr_image_data).decode('utf-8')
    #     context['qr_image_base64'] = qr_image_base64
    #     context['variable'] = qr_text
    # return render(request, 'index.html', context=context)
    
    if request.method == "POST":
        qr_text = request.POST.get("qr_text","")
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=15,
            border=1,
        )
        qr.add_data(qr_text)
        qr.add_data("This is the way")
        qr.make(fit=True)
        qr_image_pil = qr.make_image(fill_color="black",back_color="white")
    
    # Convert QR code image to base64 format
        stream = BytesIO()
        qr_image_pil.save(stream, format='PNG')
        qr_image_data = stream.getvalue()
        qr_image_base64 = base64.b64encode(qr_image_data).decode('utf-8')
        
        # Store data in context to send to the template
        context['qr_image_base64'] = qr_image_base64
        context['variable'] = qr_text
        
    return render(request, 'index.html', context=context)


def scan_view(request):
    form = ScanForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        scanned_data = form.cleaned_data.get('isbn')
        # Process the scanned data as needed
        print("This is the scanned data:",scanned_data)

        #return render(request, 'scan_form.html', {'scanned_data': scanned_data})
    
    return render(request, 'scan_form2.html', {'form': form})

