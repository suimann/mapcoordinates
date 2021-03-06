from maps.models import Map, Location, Link
from django.contrib import admin

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
admin.site.register(Link, LinkAdmin)

