from django.conf.urls import patterns, url
from django.views.generic import RedirectView
from base.views import Generic
from base.models import Pomysl, Okres, Blad, Tradycja

urlpatterns = patterns('base.views',
    url(r'^$', 'oprojekcie', name='about'),
    url(r'^kontakt/$', 'kontakt', name='contact'),
    url(r'^o_projekcie/$', 'oprojekcie', name='about'),
    url(r'^supermarket/$', 'supermarket', name='supermarket'),
    url(r'raw/okres/(?P<okres_pk>\d+)/$','okres_raw', name='okres_raw'),
    url(r'raw/narzedzie/(?P<narzedzie_pk>\d+)/(?P<cat>[a-zA-Z0-9_]+)/$','narzedzie_raw', name='narzedzie_raw'),
    url(r'raw/pomysl/(?P<obj_pk>\d+)/$','propozycja_raw',{'obj_class' : Pomysl}, name='propozycja_raw'),
    url(r'raw/blad/(?P<obj_pk>\d+)/$','propozycja_raw',{'obj_class' : Blad}, name='propozycja_raw'),
    url(r'raw/tradycja/(?P<obj_pk>\d+)/$','propozycja_raw',{'obj_class' : Tradycja}, name='propozycja_raw'),
)