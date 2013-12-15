from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from base.models import Pomysl, Forma, Okres, Blad, Tradycja
from django.template import RequestContext
from django.views.generic.list import ListView
from django.utils import timezone
from django import forms
from recaptchawidget.fields import ReCaptchaField


class ReCaptchaForm(forms.Form):
    recaptcha = ReCaptchaField()


class Generic(ListView):
    def get_context_data(self, **kwargs):
        context = super(Generic, self).get_context_data(**kwargs)
        context.__class__
        return context

def home(request):
    return render_to_response('base/home.html', {})


def supermarket(request):
    data = {'object_list': Okres.objects.all(), 'max': Okres.objects.count() - 1}
    return render_to_response('base/supermarket.html', data)


def kontakt(request):
    return render_to_response('base/kontakt.html', {})


def dodaj(request):
    """
    It is pointless to valid form fields in django. Minimal validation implemented in JS.
    """
    captcha = ReCaptchaForm()
    if request.method == 'POST':
        form = ReCaptchaForm(request.POST)
        if form.is_valid():
            return render_to_response('base/add_form.html', {'cap': captcha, 'toast': True, 'success': True},
                                      context_instance=RequestContext(request))
        else:
            return render_to_response('base/add_form.html', {'cap': captcha, 'toast': True, 'success': False},
                                      context_instance=RequestContext(request))
    else:
        return render_to_response('base/add_form.html', {'cap': captcha}, context_instance=RequestContext(request))


def ocena(request):
    return render_to_response('base/home.html', {})


def pomysl(request):
    return render_to_response('base/home.html', {})


def pomysl_detal(request, pomysl_pk, raw=False):
    obj = get_object_or_404(Pomysl, pk=pomysl_pk)
    if not raw:
        data = {'pomysl': obj, 'blady': obj.blady.all(), 'tradycje': obj.tradycja.all()}
        return render_to_response('base/pomysl_detal.html', data)
    else:
        return render_to_response('base/pomysl_raw.html', {'pomysl': obj})


def formy_dla_okresu(request, okres_pk):
    okres = get_object_or_404(Okres, pk=okres_pk)
    return render_to_response('base/formy.html', {'forma': okres.forma.all()})


def tradycja_detal(request, tradycja_pk, raw=False):
    obj = get_object_or_404(Tradycja, pk=tradycja_pk)
    if not raw:
        return render_to_response('base/tradycja_detal.html', {'tradycja': obj})
    else:
        return render_to_response('base/tradycja_raw.html', {'tradycja': obj})


def blad_detal(request, blad_pk, raw=False):
    obj = get_object_or_404(Blad, pk=blad_pk)
    if not raw:
        return render_to_response('base/blad_detal.html', {'blad': obj})
    else:
        return render_to_response('base/blad_raw.html', {'blad': obj})


def oprojekcie(request):
    return render_to_response('base/about.html', {})


def forma_detal(request, forma_pk):
    obj = get_object_or_404(Forma, pk=forma_pk)
    data = {'forma': obj, 'pomysly': obj.pomysl_set.all()}
    return render_to_response('base/forma_detal.html', data)
