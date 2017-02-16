from django.contrib import admin
from .models import AdicionalInformation

class AdicionalInformationAdmin(admin.ModelAdmin):
  list_display = ['address', 'phone', 'email', 'created_at']
  list_filter = ['created_at']

admin.site.register(AdicionalInformation, AdicionalInformationAdmin)
