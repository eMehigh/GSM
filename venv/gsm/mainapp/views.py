from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .models import Product
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def index(request):
    return render(request, 'mainapp/index.html')


@csrf_exempt
def shop(request):
    products = Product.objects.all().order_by('-pret')
    return render(request, 'mainapp/shop.html', {'products':products})

def info(request, **kargs):
    return render(request, 'mainapp/info.html')

def form_view(request):
    if request.method == 'POST':
        name = request.POST['nume']
        subiect = request.POST['subiect']
        phone = request.POST['phone-number']
        email = request.POST['email']
        message = request.POST['message']
        if name and subiect and phone and email and message:
            mail_message = f'{name} \n\n {phone} \n\n {email} \n\n {message}'
            print(mail_message)
            send_mail(subiect,
                    mail_message, 
                    'paraschiva.mihai29@gmail.com',
                    ['mihaieugen999@gmail.com']
            )
        else:
            messages.info(request, 'Informații invalide.')
            redirect('mainapp/form.html', messages)
    return render(request, 'mainapp/form.html')
