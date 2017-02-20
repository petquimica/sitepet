from django.shortcuts import render
from django.contrib import messages
from information.models import Information
from gallery.models import Gallery
from .forms import ContactForm


def home(request):
  template = 'core/home.html'
  informations = Information.objects.all()[:3]
  recent = get_recent_picture()
  gallery = Gallery.objects.filter(recent_picture=False)[:2]
  context = {
    'recent': recent,
    'informations': informations,
    'gallery': gallery,
  }
  send_email(request, context)
  return render(request, template, context)


def send_email(request, context):
  form = ContactForm(request.POST or None)
  if form.is_valid():
    form.send_message()
    messages.success(request, "Seu email foi enviado com sucesso")
  context['form'] = form

def get_recent_picture():
  gallery = Gallery.objects.all()
  image = Gallery.objects.latest('created_at')
  image.recent_picture = True
  image.save()
  gallery = Gallery.objects.all()[1:]
  for photo in gallery:
    photo.recent_picture = False
    photo.save()
  return image
