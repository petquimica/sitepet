from django.conf.urls import url
from . import views

app_name = 'project'
urlpatterns = [
  url(r'^$', views.IndexView.as_view(), name="index"),
  url(r'^(?P<slug>[\w_-]+)/$', views.ProjectView.as_view(), name="details"),
]
