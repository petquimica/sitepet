from django.contrib import admin
from .models import Project


class ProjectAdmin(admin.ModelAdmin):
  fields = ['title', 'content', 'link']
  list_display = ['title', 'created_at']
  search_fields = ['title', 'content']
  list_filter = ['created_at']


admin.site.register(Project, ProjectAdmin)
