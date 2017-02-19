from django.shortcuts import render
from django.views.generic import View
from .models import Team


class TeamView(View):
  template = 'team/team.html'

  def get(self, request):
    team = Team.objects.all()
    context = {'team': team}
    return render(request, self.template)
