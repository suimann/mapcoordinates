from django.db import models

# locations zum Testen nachgebaut
class Location(models.Model):
    entity_id = models.CharField(max_length=8)
    name = models.CharField(max_length=3)
    def __unicode__(self):
        return self.name
        
class Coordinate(models.Model):
    location = models.ForeignKey(Location)
    coordinate = models.CharField(max_length=9)
    def __unicode__():
        return self.coordinate    