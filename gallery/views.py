from django.views.generic import ListView
from .models import Gallery


class GalleryView(ListView):
    model = Gallery
    context_object_name = 'gallery'
    paginate_by = 8
    template_name = 'gallery/gallery.html'


class GalleryImageView(ListView):
    model = Gallery
    paginate_by = 16
    template_name = 'gallery/gallery_images.html'

    def get_queryset(self):
        # get the url slug
        slug = self.kwargs.get('slug', '')
        # get all folders with specific slug, they will return only one
        queryset = Gallery.objects.filter(slug__icontains=slug)
        # get the returned folder and get all images of it
        queryset = queryset.first().images.all()
        return queryset

    def get_context_data(self):
        # Get the context of class
        context = super(ListView, self).get_context_data()
        # Get the url slug
        slug = self.kwargs.get('slug', '')
        # get the gallery of specific slug
        gallery = Gallery.objects.get(slug=slug)
        # if gallery exists add on context
        if gallery:
            context['gallery'] = gallery
        return context
