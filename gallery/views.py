from django.views.generic import ListView
from .models import Gallery


class GalleryView(ListView):
    model = Gallery
    context_object_name = 'gallery'
    paginate_by = 12
    template_name = 'gallery/gallery.html'
