from django.conf.urls import patterns, url
from django.views.generic import RedirectView
from base.views import Generic
from base import views
from base.models import Pomysl, Okres, Blad, Tradycja


urlpatterns = patterns('base.views',
    url(r'^$', 'oprojekcie', name='about'),
    url(r'^co_nowego/$', 'post_list', name='news'),
    url(r'^co_nowego/(?P<pk>[0-9]+)/$', views.post_detail, name='news_detail'),
    url(r'^news/new/$', views.post_new, name='post_new'),
    url(r'^news/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    #url(r'^tradycja/(?P<pk>[0-9]+)/edit/$', views.tradycja_edit, name='tradycja_edit'),
    url(r'^kontakt/$', 'kontakt', name='contact'),
    url(r'^moderuj/$', 'moderuj', name='moderuj'),
    url(r'^zarzadzaj/$', 'zarzadzaj', name='zarzadzaj'),
    url(r'^pomysly/$', 'pomysly', name='pomysly'),
    url(r'^rejestruj/$', 'rejestruj', name='rejestruj'),
    url(r'^o_projekcie/$', 'oprojekcie', name='about'),
    url(r'^logowanie/$', 'logowanie', name='logowanie'),
    url(r'^zaproponuj/$', 'zaproponuj', name='zaproponuj'),
    url(r'^supermarket/$', 'supermarket', name='supermarket'),
    url(r'^wylogowanie/$', 'wylogowanie', name='wylogowanie'),
    #raw
    url(r'raw/okres/(?P<okres_pk>\d+)/$','okres_raw', name='okres_raw'),
    url(r'raw/komentarz/$','komentarz_raw', name='komentarz_raw'),
    url(r'raw/komentarz/(?P<obj_pk>\d+)/$','komentarz_raw', name='komentarz_raw'),
    url(r'raw/bledy/(?P<obj_pk>\d+)/$','propozycja_raw', name='propozycja_raw'),
    url(r'raw/pomysl/(?P<obj_pk>\d+)/$','propozycja_raw', name='propozycja_raw'),
    url(r'raw/tradycja/(?P<obj_pk>\d+)/$','propozycja_raw', name='propozycja_raw'),
    url(r'raw/narzedzie/(?P<narzedzie_pk>\d+)/$','narzedzie_dsc_raw', name='narzedzie_dsc_raw'),
    url(r'raw/narzedzie/(?P<narzedzie_pk>\d+)/(?P<cat>[a-zA-Z0-9_]+)/$','narzedzie_raw', name='narzedzie_raw'),
    url(r'raw/komentarz/nowy/(?P<prop_pk>\d+)/$','komentarz_raw', {'obj_pk': 'nowy'}, name='komentarz_raw_nowy'),
)















