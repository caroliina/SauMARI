# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.

from .models import Listing, Type, Image, Clothing
    
class ListingAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Hind',               {'fields': ['price']}),
        ('Töö iseloomustus', {'fields': ['description']}),
        ('Tüüp', {'fields': ['type']}),
    ] 
    
class ImageAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Pilt',               {'fields': ['image']}),
        ('Kirjeldus', {'fields': ['img_description']}),
        ('Hind', {'fields': ['price']}),
        ('Tüüp', {'fields': ['img_type']}),
    ] 

admin.site.register(Type)
admin.site.register(Clothing)
admin.site.register(Listing, ListingAdmin)
admin.site.register(Image, ImageAdmin)