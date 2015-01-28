# -*- coding: UTF-8 -*-
from django.http import HttpResponse, HttpResponseBadRequest
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, get_object_or_404
from base.models import Pomysl, Okres, Blad, Tradycja, Rok, Narzedzia, Propozycja, Komentarz
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.views.generic.list import ListView
from django.http import HttpResponseRedirect
from django.contrib.auth.models import Group
from base.forms import PropozycjaForm, KomentarzForm, RejestracjaForm
from django import forms
from recaptchawidget.fields import ReCaptchaField
from django.contrib.auth.decorators import login_required, user_passes_test
from django.forms import ValidationError
from django.db import transaction
from datetime import datetime


def is_moderator(user):
    moderator_group, created = Group.objects.get_or_create(name='Edytor')
    return moderator_group in user.groups.all()


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


@login_required
def zaproponuj(request):
    data = {}

    if request.method == 'POST':
        form = PropozycjaForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                try:
                    success = True
                    print form.cleaned_data
                    narzedzie = form.cleaned_data['narzedzie']
                    if not narzedzie or narzedzie == '':
                        narzedzie_opis = form.cleaned_data['narzedzie_opis']
                        narzedzie_nazwa = form.cleaned_data['narzedzie_nazwa']
                        if narzedzie_opis and narzedzie_nazwa:
                            narzedzie = Narzedzia.objects.create(dodana_przez=request.user, opis=narzedzie_opis,
                                                                 nazwa=narzedzie_nazwa)
                            form.cleaned_data['narzedzie_okres'].narzedzia.add(narzedzie)
                        else:
                            raise ValidationError('narzedzie_opis or narzedzie_nazwa has empty value')
                    model = form.cleaned_data['model']
                    create_dict = {
                        'narzedzie': narzedzie,
                        'nazwa': form.cleaned_data['nazwa'],
                        'druzyna': form.cleaned_data['druzyna'],
                        'opis': form.cleaned_data['opis'],
                        'moment_wystapienia': form.cleaned_data['moment_wystapienia'],
                        'dodana_przez': request.user,
                        '_autor': form.cleaned_data['_autor']
                    }
                    if model == u'Pomysł':
                        obj = Pomysl.objects.create(**create_dict)
                    elif model == u'Błąd':
                        obj = Blad.objects.create(**create_dict)
                    elif model == u'Tradycja':
                        obj = Tradycja.objects.create(**create_dict)
                    form = PropozycjaForm()
                except:
                    import sys, traceback

                    traceback.print_exc(file=sys.stdout)
                    success = False
        else:
            success = False
        data['success'] = success
    else:
        form = PropozycjaForm()
    data['form'] = form
    return render_to_response('base/zaproponuj.html', data, context_instance=RequestContext(request))


@login_required
@user_passes_test(is_moderator)
def moderuj(request):
    zle = []
    if request.method == 'POST':
        do_zaakceptowania_narzedzia = request.POST.getlist('accept_narzedzia', [])
        Narzedzia.objects.filter(pk__in=do_zaakceptowania_narzedzia).update(zaakceptowany=True)
        do_zaakceptowania = request.POST.getlist('accept', [])
        zle = Propozycja.objects.filter(pk__in=do_zaakceptowania, narzedzie__zaakceptowany=False).values_list('id',
                                                                                                              flat=True)
        # Propozycja.objects.filter(pk__in=do_zaakceptowania).exclude(pk__in=zle).update(zaakceptowany=True)
        # Not work with mysql db. django ticket #20300
        for p in Propozycja.objects.filter(pk__in=do_zaakceptowania).exclude(pk__in=zle):
            p.zaakceptowany = True
            p.save()
    not_accepted = Propozycja.objects.filter(zaakceptowany=False)
    data = {
        'zle': zle,
        'narzedzie': Narzedzia.objects.filter(zaakceptowany=False),
        'pomysl': not_accepted.instance_of(Pomysl),
        'blad': not_accepted.instance_of(Blad),
        'tradycja': not_accepted.instance_of(Tradycja),
    }
    return render_to_response('base/moderuj.html', data, context_instance=RequestContext(request))


def rejestruj(request):
    data = {}
    if request.method == 'POST':
        form = RejestracjaForm(request.POST)
        if form.is_valid():
            data = {
                'first_name': form.cleaned_data['imie'],
                'last_name': form.cleaned_data['nazwisko'],
                'username': form.cleaned_data['username'],
                'email': form.cleaned_data['mail'],
            }
            try:
                user = User.objects.create_user(**data)
                user.set_password(form.cleaned_data['password'])
                user.is_active = True
                user.save()
                data['success'] = True
            except:
                errors = form._errors.setdefault("myfield", ErrorList())
                errors.append(u"Użytkownik już istnieje!")
    else:
        form = RejestracjaForm()
    data['form'] = form
    return render_to_response('base/rejestruj.html', data, context_instance=RequestContext(request))


def supermarket(request):
    data = {'okresy': Okres.objects.all(), 'lata': Rok.objects.all()}
    return render_to_response('base/supermarket.html', data, context_instance=RequestContext(request))


def kontakt(request):
    return render_to_response('base/kontakt.html', context_instance=RequestContext(request))


# ajax part
def okres_raw(request, okres_pk):
    okres = get_object_or_404(Okres, pk=okres_pk)
    data = {'narzedzia': okres.narzedzia.filter(zaakceptowany=True).all()}
    return render_to_response('base/okres_raw.html', data, context_instance=RequestContext(request))


def narzedzie_dsc_raw(request, narzedzie_pk, ):
    narzedzie = get_object_or_404(Narzedzia, pk=narzedzie_pk)
    return HttpResponse(narzedzie.opis)


def narzedzie_raw(request, narzedzie_pk, cat):
    narzedzie = get_object_or_404(Narzedzia, pk=narzedzie_pk)
    if cat == 'latest':
        obj_list = narzedzie.propozycja_set.filter(zaakceptowany=True).instance_of(Pomysl).order_by('-pk')
    elif cat == 'top_rated':
        obj_list = sorted(narzedzie.propozycja_set.filter(zaakceptowany=True).instance_of(Pomysl).all(),
                          key=lambda a: a.rate)
    elif cat == 'bugs':
        obj_list = narzedzie.propozycja_set.filter(zaakceptowany=True).instance_of(Blad).order_by('-pk')
    elif cat == 'tradition':
        obj_list = narzedzie.propozycja_set.filter(zaakceptowany=True).instance_of(Tradycja).order_by('-pk')
    else:
        obj_list = []
    data = {
        'cat': cat,
        'objects': obj_list
    }
    return render_to_response('base/narzedzie_raw.html', data, context_instance=RequestContext(request))


def komentarz_raw(request, obj_pk=None, prop_pk=None):
    form = None
    if request.method == 'POST':
        form = KomentarzForm(request.POST)
        if form.is_valid() and request.user:
            Komentarz.objects.create(
                autor=request.user,
                zawartosc=form.cleaned_data['zawartosc'],
                data_publikacji=datetime.now(),
                propozycja=form.cleaned_data['propozycja'],
                ocena=form.cleaned_data['ocena']
            )
    else:
        if prop_pk:
            form = KomentarzForm(propozycja=get_object_or_404(Propozycja, pk=prop_pk))
    if obj_pk:
        if obj_pk == 'nowy':
            return render_to_response('base/komentarz_form_raw.html', {'form': form, 'prop_pk': prop_pk},
                                      context_instance=RequestContext(request))
        else:
            obj = get_object_or_404(Komentarz, pk=obj_pk)
            return render_to_response('base/komentarz_raw.html', {'komentarz': obj},
                                      context_instance=RequestContext(request))
    else:
        propozycja = request.GET.get('propozycja', None)
        obj_list = Komentarz.objects.all()
        if propozycja:
            obj_list = obj_list.filter(propozycja__pk=propozycja)
        return render_to_response('base/komentarz_list_raw.html', {'komentarze': obj_list},
                                  context_instance=RequestContext(request))


def propozycja_raw(request, obj_pk):
    propozycja = get_object_or_404(Propozycja, pk=obj_pk)
    data = {
        'propozycja': propozycja,
        'komentarze': propozycja.komentarz_set.all(),
        'komentarz_form': KomentarzForm(propozycja=propozycja),
    }
    return render_to_response('base/propozycja_raw.html', data, context_instance=RequestContext(request))


@user_passes_test(lambda u: u.is_superuser)
def zarzadzaj(request):
    data = {
        'users': User.objects.all()
    }
    if request.method == 'POST':
        type = request.POST.get('type')
        id = request.POST.get('id')
        user = get_object_or_404(User,pk=id)
        if user.pk == request.user.pk:
            return HttpResponseBadRequest()
        if type == 'moderator':
            g = Group.objects.get(name='Edytor')
            if user.groups.filter(name='Edytor').exists():
                g.user_set.remove(user)
            else:
                g.user_set.add(user)
        elif type == 'administrator':
            if user.is_superuser:
                user.is_superuser = False
            else:
                user.is_superuser = True
            user.save()
        elif type == 'remove':
            user.delete()
        return HttpResponse()
    return render_to_response('base/zarzadzaj.html', data, context_instance=RequestContext(request))


def pomysly(request):
    data = {
        'narzedzia' : Narzedzia.objects.filter(zaakceptowany=True)
    }
    return render_to_response('base/pomysly.html', data, context_instance=RequestContext(request))