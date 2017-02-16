from django.contrib import admin
from .models import Information, File, Link


class FileInlineAdmin(admin.StackedInline):
  model = File
  prepopulated_fields = {'slug': ('title',)}


class LinkInlineAdmin(admin.TabularInline):
  model = Link


class InformationAdmin(admin.ModelAdmin):
  list_display = ['title', 'slug', 'created_at']
  search_fields = ['title', 'content']
  list_filter = ['created_at']
  prepopulated_fields = {'slug': ('title',)}
  inlines = [FileInlineAdmin, LinkInlineAdmin]


admin.site.register(Information, InformationAdmin)
