from django.conf.urls import url
from . import views


app_name = 'gallery'
urlpatterns = [
    url(r'^$', views.GalleryView.as_view(), name='gallery'),
]
