from django.shortcuts import render_to_response
from maps.models import Map, Location, Link
from django.template import RequestContext

def index(request):
    map_list = Map.objects.all().order_by('-map_name')
    location_list = Location.objects.all().order_by('-location_name')
    link_list = Link.objects.all()
    return render_to_response('maps/index.html', {'map_list': map_list, 'location_list': location_list, 'link_list': link_list},context_instance=RequestContext(request))
    #return render_to_response('maps/index.html', {'map_list': map_list, 'location_list': location_list},context_instance=RequestContext(request))