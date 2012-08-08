from django.db import models

class Map(models.Model):
    map_name = models.CharField(max_length=50)    
    map_url = models.CharField(max_length=1000)

    def __unicode__(self):
        return self.map_name



class Location(models.Model):
    location_name = models.CharField(max_length=20)
    
    def __unicode__(self):
        return self.location_name



class Link(models.Model):
    map = models.ForeignKey(Map)
    location = models.ForeignKey(Location)        
    link_coordinate = models.CharField(max_length=15,blank=True, null=True)

    def __unicode__(self):
        return "Karte= \"" + self.map.map_name + "\" Raum= \"" + self.location.location_name +"\""
