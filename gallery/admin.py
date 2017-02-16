from django.contrib import admin
from .models import Gallery


class GalleryAdmin(admin.ModelAdmin):
  fields = ['title', 'description', 'image']
  list_display = ['title', 'created_at']
  search_fields = ['title', 'description']
  list_filter = ['created_at']


admin.site.register(Gallery, GalleryAdmin)
