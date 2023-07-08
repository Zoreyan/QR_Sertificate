from django.shortcuts import render, redirect
from .forms import SertificateForm, SettingsForm
from .models import Sertificate, Settings
from PIL import Image, ImageDraw, ImageFont
import qrcode
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# User Login

def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
        context = {}
        return render(request, 'qr/login.html', context)

# User Logout
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def home(request):
    context = {

    }
    return render(request, 'qr/index.html', context)

@login_required(login_url='login')
def sertificate_form(request):
    form = SertificateForm()
    if request.method == 'POST':
        form = SertificateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('sertificate-list')
        
    context = {
        'form': form
    }
    return render(request, 'qr/sertificate_form.html', context)

@login_required(login_url='login')
def sertificate_list(request):
    sertificates = Sertificate.objects.all()
    context = {
        'sertificates': sertificates
    }
    return render(request, 'qr/sertificate_list.html', context)


def sertificate_detail(request, pk):
    sertificate = Sertificate.objects.get(id=pk)
    form = SertificateForm(instance=sertificate)
    name = sertificate.name
    sertificate_template = sertificate.settings.template.path
    x = sertificate.settings.x
    y = sertificate.settings.y
    font_size = sertificate.settings.font_size

    if request.method == 'POST':
        form = SertificateForm(request.POST, request.FILES, instance=sertificate)
        if form.is_valid():
            # 
            font = ImageFont.truetype("arial.ttf", size=font_size)
            image = Image.open(f'{sertificate_template}')
            draw = ImageDraw.Draw(image)
            draw.text((x, y), name, font=font, fill=(0,0,0,0))
            #
            qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
                )
            qr.add_data(f'https://www.example.com/sertificate-detail/{pk}')
            qr.make(fit=True)
            qr_image = qr.make_image(fill_color="black", back_color="white")

            # Масштабирование и добавление QR-кода к изображению
            template_width, template_height = image.size
            print(template_width, template_height)
            qr_image = qr_image.resize((100, 100))
            image.paste(qr_image, (template_width-100, template_height-100))

            bytes_io = BytesIO()
            image.save(bytes_io, format='JPEG')
            file = InMemoryUploadedFile(bytes_io, None, 'image.jpg', 'image/jpeg', bytes_io.getbuffer().nbytes, None)
            form.instance.image = file
            form.save()
            return redirect('sertificate-detail',  pk=pk)

    context = {
        'sertificate': sertificate,
        'form': form
    }
    return render(request, 'qr/sertificate_detail.html', context)


@login_required(login_url='login')
def settings(request):
    form = SettingsForm()
    if request.method == 'POST':
        form = SettingsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    context = {
        'form': form
    }
    return render(request, 'qr/settings.html', context)