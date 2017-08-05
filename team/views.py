from django.shortcuts import render
from django.views.generic import TemplateView, View
from .models import Team


class TeamView(View):
    template = 'team/team.html'

    def get(self, request):
        teacher = Team.objects.filter(is_teacher=True).first()
        team = Team.objects.filter(is_teacher=False)
        context = {'team': team, 'teacher': teacher}
        return render(request, self.template, context)


class HistoricView(TemplateView):
    template_name = 'team/historic.html'
