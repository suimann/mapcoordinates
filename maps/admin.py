from maps.models import Map, Location, Link
from django.contrib import admin
<<<<<<< HEAD
    

class LocationAdmin(admin.ModelAdmin):
    fields=['entity_id', 'name']

admin.site.register(Location, LocationAdmin)
admin.site.register(Coordinate)
=======

class MapAdmin(admin.ModelAdmin):
    fieldsets = [
    ('Map information', {'fields': ['map_name', 'map_url']}),    
    ]    
    list_display = ('map_name', 'map_url')

class LinkAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['map']}),
        ('Location', { 'fields': ['location', 'link_coordinate'] }),    
    ]
    list_display = ('map', 'location', 'link_coordinate')
    list_filter = ['map']

admin.site.register(Map, MapAdmin)
admin.site.register(Location)
<<<<<<< HEAD
admin.site.register(Link)
>>>>>>> 21eadf15c6665b9efdd15b5a3e422e268df671b6
=======
admin.site.register(Link, LinkAdmin)
>>>>>>> jan
