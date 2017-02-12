from django.shortcuts import render
from information.models import Information


def home(request):
  template = 'core/home.html'
  informations = Information.objects.all()[:3]
  context = {
    'informations': informations,
  }
  return render(request, template, context)
