from django.shortcuts import render_to_response
from maps.models import Map, Location

def index(request):
    map_list = Map.objects.all().order_by('-map_name')
    location_list = Location.objects.all().order_by('-location_name')
    return render_to_response('maps/index.html', {'map_list': map_list, 'location_list': location_list})
