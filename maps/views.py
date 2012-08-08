from django.shortcuts import render_to_response,get_object_or_404
from maps.models import Map, Location, Link
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

def index(request):
    map_list = Map.objects.all().order_by('-map_name')
    location_list = Location.objects.all().order_by('-location_name')
    link_list = Link.objects.all().order_by('-link_ccordinate')
    return render_to_response('maps/index.html', {'map_list': map_list, 'location_list': location_list, 'link_list': link_list},context_instance=RequestContext(request))
    #return render_to_response('maps/index.html', {'map_list': map_list, 'location_list': location_list},context_instance=RequestContext(request))
	
def saveindb(request):
    l = get_object_or_404(Link)
    try:
	    selected_choice = l.links_set.get(pk=request.POST['link_coordinates'])
	    return render_to_response('', {
		    'error_message': "test",
			}, context_instance=RequestContext(request))
    except (KeyError, Link.DoesNotExist):
	    return render_to_response('', {
		    'error_message': "fehler",
			}, context_instance=RequestContext(request))
    else:
	    return render_to_response('', {
		    'error_message': "blubb",
			}, context_instance=RequestContext(request))
	    selected_choice.save()
	    return HttpResponseRedirect(reverse('', args=(l.id,)))