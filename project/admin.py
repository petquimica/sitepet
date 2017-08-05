from django.contrib import admin
from .models import Project


class ProjectAdmin(admin.ModelAdmin):
    fields = ['title', 'slug', 'content', 'link']
    list_display = ['title', 'slug', 'created_at']
    search_fields = ['title', 'content']
    list_filter = ['created_at']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Project, ProjectAdmin)
