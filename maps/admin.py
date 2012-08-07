from maps.models import Location, Coordinate
from django.contrib import admin

class CoordinateInLine(admin.StackedInLine)

class LocationAdmin(admin.ModelAdmin):
    fields=['entity_id', 'name']

admin.site.register(Location, LocationAdmin)
admin.site.register(Coordinate)