from django.contrib import admin
from .models import Gallery, Image


class ImageInlineAdmin(admin.StackedInline):
    model = Image


class GalleryAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title', 'description']
    list_filter = ['created_at']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ImageInlineAdmin]


admin.site.register(Gallery, GalleryAdmin)
