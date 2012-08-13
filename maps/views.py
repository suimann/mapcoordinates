from django.shortcuts import get_object_or_404, render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.gzip import gzip_page
from django.views.decorators.http import require_safe, require_POST
from maps.models import Map, Location, Link
from django.utils import simplejson
from django.core import serializers

#------------------ Laden der Begruessungsseite ----------------------------
@csrf_exempt
def index(request):
    
    map_list = Map.objects.all().order_by('-map_name')

    return render_to_response('maps/index.html', {'map_list': map_list})
#...........................................................................

#------------------ Laden der Koordinatenseite -----------------------------
@csrf_exempt
def choose(request):
        
    #Deklaration der Variablen um die Selektion beizubehalten
    map_id = request.POST['map_id']
    map = Map.objects.get(id=map_id)

    #Holen der zu uebergebenen Standard Daten aus der Datenbank.
    location_list = Location.objects.all().order_by('-location_name')
        
    # Zur weiteren Verarbeitung der link-Liste wird sie in json umgewandelt
    coordinates_list_data = serializers.serialize("json", Link.objects.filter(map_id=map.id).all())
    json_list = simplejson.dumps(coordinates_list_data)

    return render_to_response('maps/choose_coords.html', {'map': map, 'location_list': location_list, 'coordinates_list_data': coordinates_list_data})
#...........................................................................

#----------------------Speichern der Koordinaten ---------------------------
@csrf_exempt
def save(request):

    #Deklaration der Variablen um die Selektion beizubehalten
    map_id = request.POST['map_id']
    #map = Map.objects.get(id=map_id)

    #Holen der zu uebergebenen Standard Daten aus der Datenbank.
    location_list = Location.objects.all().order_by('-location_name')
    
    #Speichern
    m = Map.objects.get_or_create(pk = map_id)[0]
    m.save()
   
    print('location:' + request.POST['location_name'])   
    
    loc = Location.objects.get_or_create(pk= request.POST['location_name'])[0]
    loc.save()   
    
    print(loc)
    print(m)
    print(request.POST['coords'])    
    
    l = Link.objects.get_or_create(map=m, location=loc)[0]   
    l.link_coordinate = request.POST['coords']    
    l.save()
    
    #p = Link(map_id=request.POST['map_id'], location_id=request.POST['location_name'], link_coordinate=request.POST['coords'])
    #p.save()

    # Zur weiteren Verarbeitung der link-Liste wird sie in json umgewandelt
    coordinates_list_data = serializers.serialize("json", Link.objects.filter(map=m).all())
    json_list = simplejson.dumps(coordinates_list_data)
    
    return render_to_response('maps/choose_coords.html', {'map': m, 'location_list': location_list, 'coordinates_list_data': coordinates_list_data})
    
#...........................................................................








