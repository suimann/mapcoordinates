from django.shortcuts import get_object_or_404, render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.gzip import gzip_page
from django.views.decorators.http import require_safe, require_POST
from maps.models import Map, Location, Link

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

    #Holen der zu uebergebenen Standard Daten aus der Datenbank
    location_list = Location.objects.all().order_by('-location_name')
    coordinates_list = Link.objects.all()

    return render_to_response('maps/choose_coords.html', {'map': map, 'location_list': location_list, 'coordinates_list': coordinates_list})
#...........................................................................

#----------------------Speichern der Koordinaten ---------------------------
@csrf_exempt
def save(request):

    #Deklaration der Variablen um die Selektion beizubehalten
    map_id = request.POST['map_id']
    map = Map.objects.get(id=map_id)

    #Holen der zu uebergebenen Standard Daten aus der Datenbank
    location_list = Location.objects.all().order_by('-location_name')
    coordinates_list = Link.objects.all()

    return render_to_response('maps/choose_coords.html', {'map': map, 'location_list': location_list, 'coordinates_list': coordinates_list})
    
#...........................................................................








