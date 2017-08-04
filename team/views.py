from django.views.generic import TemplateView


class TeamView(TemplateView):
    template_name = 'team/team.html'


class HistoricView(TemplateView):
    template_name = 'team/historic.html'
