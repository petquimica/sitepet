from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from .models import Information


class IndexView(ListView):
  paginate_by = 6
  template_name = 'information/index.html'

  def get_queryset(self):
    queryset = Information.objects.all()
    tag = self.kwargs.get('tag', '')
    if tag:
      queryset = queryset.filter(tags__slug__icontains=tag)
    return queryset

  def get_context_data(self):
    context = super(IndexView, self).get_context_data()
    tag = self.kwargs.get('tag', '')
    if tag:
      context['tag'] = tag
    return context


class InformationView(DetailView):
  model = Information
  template_name = 'information/details.html'
