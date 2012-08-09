from maps.models import Map, Location, Link
from django.contrib import admin
<<<<<<< HEAD
    

class LocationAdmin(admin.ModelAdmin):
    fields=['entity_id', 'name']

admin.site.register(Location, LocationAdmin)
admin.site.register(Coordinate)
=======

admin.site.register(Map)
admin.site.register(Location)
admin.site.register(Link)
>>>>>>> 21eadf15c6665b9efdd15b5a3e422e268df671b6
