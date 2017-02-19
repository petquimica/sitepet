from django.conf.urls import url
from . import views

app_name = 'team'
urlpatterns = [
  url(r'^$', views.TeamView.as_view(), name='team'),
]
