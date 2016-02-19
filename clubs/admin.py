from django.contrib import admin
from .models import Club
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy
"""
This class allows me to set a custom order and organization for
how I want my admin panel for clubs to be displayed.
It's a good idea because my users will be editing this file. 
"""
class ClubAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        ('Contact Information', {'fields': ['contact_person',
                                            'contact_email', 'club_website']}),
        ('Images', {'fields': ['cover_image', 'image_1', 'image_2', 'image_3']}),
        ('Descriptions', {'fields': ['category', 'tagline', 'description']})
    ]

admin.site.register(Club, ClubAdmin)
