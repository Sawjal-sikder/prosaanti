from django.contrib import admin
from .models import Website

@admin.register(Website)
class WebsiteAdmin(admin.ModelAdmin):
      list_display = ('name', 'email', 'phone', 'website')
      search_fields = ('name', 'email', 'phone', 'website')
      list_filter = ('name', 'email', 'phone', 'website')
      ordering = ('name',)