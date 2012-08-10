from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Path to Coordinate Form
    url(r'^maps/$', 'maps.views.index'),
    url(r'^maps/choose_coords/$', 'maps.views.choose'),
    #url(r'^maps/setter/$', 'maps.views.setter'),
    # Examples:
    # url(r'^$', 'MapCoordinates.views.home', name='home'),
    # url(r'^MapCoordinates/', include('MapCoordinates.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
