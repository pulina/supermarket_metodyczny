# -*- coding: UTF-8 -*-
from django import forms
from base.models import Okres, Narzedzia, Pomysl, Blad, Tradycja, Propozycja
from django.forms.widgets import Textarea, HiddenInput
from django.contrib.admin.widgets import RelatedFieldWidgetWrapper
from django.db.models.fields.related import ManyToManyRel


class NarzedzieForm(forms.Form):
    narzedzie = forms.ModelChoiceField(queryset=Okres.objects.all(), empty_label=None)
    nazwa = forms.CharField()
    opis = forms.CharField(widget=Textarea)


class PropozycjaForm(forms.Form):
    MODEL = (
        ('',''),
        ('Pomysł', 'Pomysł nowego narzędzia'),
        ('Tradycja', 'Tradycję związaną z istniejącym narzędziem'),
        ('Błąd', 'Błąd związany z istniejącym narzędziem'),


    )
    model = forms.ChoiceField(choices=MODEL, label='Co chcesz zaproponować')
    narzedzie = forms.ModelChoiceField(queryset=Narzedzia.objects.all(), empty_label='Chcę zaproponować nowy',
                                       label='Narzędzie metodyczne', required=False)
    narzedzie_okres = forms.ModelChoiceField(queryset=Okres.objects.all(), empty_label=None, label='Okres którego dotyczy narzędzie', required=False)
    narzedzie_nazwa = forms.CharField(label='Nazwa narzędzia', required=False)
    narzedzie_opis = forms.CharField(widget=Textarea, label='Opis narzędzia', required=False)
    pomysl = forms.ModelChoiceField(queryset=Pomysl.objects.all(), empty_label='', label='Pomysł którego to dotyczy', required=False)
    nazwa = forms.CharField(label='Nazwa propozycji')
    druzyna = forms.CharField(label='Nazwa dużyny')
    opis = forms.CharField(widget=Textarea, label='Opis propozycji')



class KomentarzForm(forms.Form):
    propozycja = forms.ModelChoiceField(queryset=Propozycja.objects.all(), empty_label=None, widget=HiddenInput)
    zawartosc = forms.CharField(widget=Textarea)
    ocena = forms.IntegerField(max_value=0, min_value=10)

    def __init__(self, *args, **kwargs):
        super(PropozycjaForm, self).__init__(*args, **kwargs)
        self.fields['propozycja'].initial = kwargs.get('propozycja')
