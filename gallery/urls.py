from django.conf.urls import url
from . import views


app_name = 'gallery'
urlpatterns = [
    url(r'^$', views.GalleryView.as_view(), name='gallery'),
    url(r'^(?P<slug>[\w_-]+)/$', views.GalleryImageView.as_view(), name='images')
]
