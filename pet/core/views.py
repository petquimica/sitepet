from django.shortcuts import render
from .models import About, Footer


def home(request):
  what_we_do = About.objects.all()[0]
  about_us = About.objects.all()[1]
  footers = Footer.objects.all()
  print(footers)
  template = 'core/home.html'
  context = {
    'about_us': about_us,
    'what_we_do': what_we_do,
    'footers': footers
  }
  return render(request, template, context)
