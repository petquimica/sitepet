from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import Q
from .models import Project


class IndexView(ListView):
  paginate_by = 6
  template_name = 'project/index.html'

  def get_queryset(self):
    queryset = Project.objects.all()
    queryset = search_project(self.request, queryset)
    return queryset


def search_project(request, project_list):
  query = request.GET.get("q_project")
  if query:
    project_list = project_list.filter(
                         Q(title__icontains=query) |
                         Q(content__icontains=query)
                       ).distinct()
  return project_list

