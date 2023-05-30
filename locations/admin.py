from django.contrib import admin
from .models import Locations, LocationCategory, Attractions

admin.site.register(Locations)
admin.site.register(LocationCategory)
admin.site.register(Attractions)