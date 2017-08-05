from django.conf.urls import url
from . import views

app_name = 'team'
urlpatterns = [
  url(r'^equipe/$', views.TeamView.as_view(), name='team'),
  url(r'^historico/$', views.HistoricView.as_view(), name='historic'),
]
