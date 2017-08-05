from django.shortcuts import render
from django.contrib import messages
from information.models import Information
from gallery.models import HomeImages
from .forms import ContactForm


def home(request):
    template = 'core/home.html'
    informations = Information.objects.all()[:3]
    pictures = HomeImages.objects.all()[1:]
    context = {
        'informations': informations,
        'gallery': pictures,
        'first_picture': HomeImages.objects.all()[0]
    }
    send_email(request, context)
    return render(request, template, context)


def send_email(request, context):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.send_message()
        messages.success(request, "Seu email foi enviado com sucesso")
    context['form'] = form

