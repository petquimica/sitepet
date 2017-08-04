from django.conf.urls import url
from . import views

app_name = 'information'
urlpatterns = [
  url(r'^$', views.IndexView.as_view(), name="index"),
  url(r'^tag/(?P<tag>[\w_-]+)/$', views.IndexView.as_view(), name="index_tag"),
  url(r'^(?P<slug>[\w_-]+)/$', views.InformationView.as_view(), name="details"),
]
