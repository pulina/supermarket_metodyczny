from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from base.models import Pomysl, Okres, Blad, Tradycja, Rok, Narzedzia
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.views.generic.list import ListView
from django.http import HttpResponseRedirect
from django.utils import timezone
from django import forms
from recaptchawidget.fields import ReCaptchaField


class ReCaptchaForm(forms.Form):
    recaptcha = ReCaptchaField()


class Generic(ListView):
    def get_context_data(self, **kwargs):
        context = super(Generic, self).get_context_data(**kwargs)
        context['has_url'] = hasattr(self.model, 'get_absolute_url')
        return context


def logowanie(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        profile = authenticate(username=username, password=password)
        if profile is not None:
            login(request, profile)
            return HttpResponseRedirect('/')
        else:
            return render_to_response('base/login.html', {'fail': True}, context_instance=RequestContext(request))
    else:
        return render_to_response('base/login.html', context_instance=RequestContext(request))


def wylogowanie(request):
    logout(request)
    return HttpResponseRedirect('/')


def oprojekcie(request):
    return render_to_response('base/about.html', context_instance=RequestContext(request))


def supermarket(request):
    data = {'okresy': Okres.objects.all(), 'lata': Rok.objects.all()}
    return render_to_response('base/supermarket.html', data, context_instance=RequestContext(request))


def kontakt(request):
    return render_to_response('base/kontakt.html', context_instance=RequestContext(request))


# ajax part
def okres_raw(request, okres_pk):
    okres = get_object_or_404(Okres, pk=okres_pk)
    data = {'narzedzia': okres.narzedzia.all()}
    return render_to_response('base/okres_raw.html', data, context_instance=RequestContext(request))


def narzedzie_raw(request, narzedzie_pk, cat):
    narzedzie = get_object_or_404(Narzedzia, pk=narzedzie_pk)
    if cat == 'latest':
        obj_list = narzedzie.propozycja_set.instance_of(Pomysl).order_by('-pk')
    elif cat == 'top_rated':
        obj_list = sorted(narzedzie.propozycja_set.instance_of(Pomysl).all(), key=lambda a: a.rate)
    elif cat == 'bugs':
        obj_list = narzedzie.propozycja_set.instance_of(Blad).order_by('-pk')
    elif cat == 'tradition':
        obj_list = narzedzie.propozycja_set.instance_of(Tradycja).order_by('-pk')
    else:
        obj_list = []
    data = {
        'cat': cat,
        'objects': obj_list
    }
    return render_to_response('base/narzedzie_raw.html', data, context_instance=RequestContext(request))


def propozycja_raw(request, obj_pk, obj_class):
    propozycja = get_object_or_404(obj_class, pk=obj_pk)
    data = {
        'propozycja': propozycja,
        'komentarze': propozycja.komentarz_set.all()
    }
    return render_to_response('base/propozycja_raw.html', data, context_instance=RequestContext(request))