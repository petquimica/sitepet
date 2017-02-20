from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('pet.core.urls')),
    url(r'^informacoes/', include('information.urls')),
    url(r'^galeria/', include('gallery.urls')),
    url(r'^', include('team.urls')),
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
