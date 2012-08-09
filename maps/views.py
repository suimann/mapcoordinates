from django.shortcuts import get_object_or_404, render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.gzip import gzip_page
from django.views.decorators.http import require_safe, require_POST
from maps.models import Map, Location, Link

@csrf_exempt
def index(request):
    if request.POST:
        print request.POST
        map = get_object_or_404(Map, map_url=request.POST['map_name'])
        p = Link(map_id=map.id, location_id=request.POST['location_name'], link_coordinate=request.POST['coords'])
        p.save()
    else:
        print "Nix GE(H)T"
    map_list = Map.objects.all().order_by('-map_name')
    location_list = Location.objects.all().order_by('-location_name')
    return render_to_response('maps/index.html', {'map_list': map_list, 'location_list': location_list})

