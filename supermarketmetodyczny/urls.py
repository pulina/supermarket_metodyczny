from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
from django.contrib import admin
from django.views.generic import RedirectView
import settings
admin.autodiscover()

urlpatterns = patterns('base.views',
    url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'home'),
    url(r'^pomysl/(?P<pomysl_pk>\d+)/$', 'pomysl_detal'),
    url(r'^pomysl/(?P<pomysl_pk>\d+)/raw/$', 'pomysl_detal',{'raw': True}),
    url(r'^blad/(?P<blad_pk>\d+)/$', 'blad_detal'),
    url(r'^blad/(?P<blad_pk>\d+)/raw/$', 'blad_detal',{'raw': True}),
    url(r'^tradycja/(?P<tradycja_pk>\d+)/$', 'tradycja_detal'),
    url(r'^tradycja/(?P<tradycja_pk>\d+)/raw/$', 'tradycja_detal',{'raw': True}),
    url(r'^pomysl/$', 'pomysl'),
    url(r'^blad/$', 'blad'),
    url(r'^tradycja/$', 'tradycja'),
    url(r'^supermarket/$', 'supermarket'),
    url(r'^supermarket/(?P<okres_pk>\d+)/$', 'formy_dla_okresu'),
    url(r'^o_projekcie/$', 'oprojekcie'),
    url(r'^dodaj/$', 'dodaj'),
    url(r'^ocena/$', 'ocena'),
    url(r'^kontakt/$', 'kontakt'),
    url(r'^na_zakupy/$', RedirectView.as_view(url='/supermarket/')),
#    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes':True}),
    url(r'^pos/', include('generic_positions.urls')),
    url(r'^forma/(?P<forma_pk>\d+)/$', 'forma_detal'),
    url(r'^forma/$', 'forma'),
)