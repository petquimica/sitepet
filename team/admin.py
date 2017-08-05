from django.contrib import admin
from .models import Team


class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_teacher', 'created_at']
    search_fields = ['name']
    list_filter = ['created_at', 'name']


admin.site.register(Team, TeamAdmin)
