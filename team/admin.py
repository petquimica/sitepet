from django.contrib import admin
from .models import Team

class TeamAdmin(admin.ModelAdmin):
  list_display = ['name', 'is_teacher', 'created_at']
  search_fields = ['name', 'description']
  list_filter = ['created_at']

# admin.site.register(Team, TeamAdmin)

