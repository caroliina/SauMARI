# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.

from .models import Listing, Type
    
class ListingAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Hind',               {'fields': ['price']}),
        ('Töö iseloomustus', {'fields': ['description']}),
        ('Tüüp', {'fields': ['type']}),
    ]   

admin.site.register(Type)
admin.site.register(Listing, ListingAdmin)