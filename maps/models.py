from django.db import models

class Map(models.Model):
    map_id = models.CharField(max_length=10)
    map_name = models.CharField(max_length=50)    
    map_url = models.CharField(max_length=1000)

    def __unicode__(self):
        return self.map_name
        
class Location(models.Model):
    map = models.ForeignKey(Map)
    room_name = models.CharField(max_length=20)
    coordinate = models.CharField(max_length=15)
    
    def __unicode__():
        return self.room_name    
