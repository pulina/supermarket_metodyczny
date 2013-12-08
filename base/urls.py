from django.conf.urls import patterns, url
from django.views.generic import RedirectView


urlpatterns = patterns('base.views',
    url(r'^$', 'home', name='home'),
    url(r'^kontakt/$', 'kontakt', name='contact'),
    url(r'^o_projekcie/$', 'oprojekcie', name='about'),

    url(r'^pomysl/$', 'pomysl', name='pomysly'),
    url(r'^pomysl/(?P<pomysl_pk>\d+)/$', 'pomysl_detal', name='pomysl'),
    url(r'^pomysl/(?P<pomysl_pk>\d+)/raw/$', 'pomysl_detal', {'raw': True}, name='pomysl_raw'),
    url(r'^blad/(?P<blad_pk>\d+)/$', 'blad_detal', name='blad'),
    url(r'^blad/(?P<blad_pk>\d+)/raw/$', 'blad_detal', {'raw': True}, name='blad_raw'),
    url(r'^tradycja/(?P<tradycja_pk>\d+)/$', 'tradycja_detal', name='tradycja'),
    url(r'^tradycja/(?P<tradycja_pk>\d+)/raw/$', 'tradycja_detal', {'raw': True},
        name='tradycja_raw'),

    url(r'^supermarket/$', 'supermarket', name='supermarket'),
    url(r'^supermarket/(?P<okres_pk>\d+)/$', 'formy_dla_okresu', name='formy'),
    url(r'^forma/(?P<forma_pk>\d+)/$', 'forma_detal', name='forma'),
    url(r'^na_zakupy/$', RedirectView.as_view(pattern_name='supermarket')),

    url(r'^dodaj/$', 'dodaj', name='dodaj'),
    url(r'^ocena/$', 'ocena', name='ocena'),
)
