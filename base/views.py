from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.shortcuts import render_to_response,  get_object_or_404
from base.models import Pomysl, Forma, Okres, STOPNIE, Blad, Tradycja
from django import template

def home(request):
    return render_to_response('base/home.html',{})

def supermarket(request):
    return render_to_response('base/supermarket.html',{'object_list': Okres.objects.all(),'stopnie':STOPNIE,'max':Okres.objects.count()-1})

def kontakt(request):
    return render_to_response('base/kontakt.html',{})

def dodaj(request):
    return render_to_response('base/home.html',{})

def ocena(request):
    return render_to_response('base/home.html',{})

def pomysl(request):
    return render_to_response('base/home.html',{})

def pomysl_detal(request,pomysl_pk,raw=False):
    obj = get_object_or_404(Pomysl,pk=pomysl_pk)
    if not raw :
        return render_to_response('base/pomysl_detal.html',{'pomysl':obj,'blady':obj.blady.all(),'tradycje':obj.tradycja.all()})
    else:
        return render_to_response('base/pomysl_raw.html',{'pomysl':obj})

def formy_dla_okresu(request,okres_pk):
    t = template.Template( """
	{% for obj in forma %}
   		 <p><a href='/forma/{{obj.pk}}'>{{ obj }}</a></p>
	{% endfor %}
	""")
    okres = get_object_or_404(Okres,pk=okres_pk)
    c = template.Context({'forma':okres.forma.all()})
    return HttpResponse(t.render(c))

def tradycja(request):
    return render_to_response('base/home.html',{})

def tradycja_detal(request,tradycja_pk,raw=False):
    obj = get_object_or_404(Tradycja,pk=tradycja_pk)
    if not raw :
        return render_to_response('base/tradycja_detal.html',{'tradycja':obj})
    else:
        return render_to_response('base/tradycja_raw.html',{'tradycja':obj})

def blad(request):
    return render_to_response('base/home.html',{})

def blad_detal(request,blad_pk,raw=False):
    obj = get_object_or_404(Blad,pk=blad_pk)
    if not raw :
        return render_to_response('base/blad_detal.html',{'blad':obj})
    else:
        return render_to_response('base/blad_raw.html',{'blad':obj})

def oprojekcie(request):
    return render_to_response('base/about.html',{})

def forma(request):
    return render_to_response('base/home.html',{})

def forma_detal(request,forma_pk):
    obj = get_object_or_404(Forma,pk=forma_pk)
    def _funkcja_slownie(self):
	return STOPNIE[self.stopien]
    return render_to_response('base/forma_detal.html',{'forma':obj,'pomysly':obj.pomysl_set.all()})
