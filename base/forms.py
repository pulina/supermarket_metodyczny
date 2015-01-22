# -*- coding: UTF-8 -*-
from django import forms
from base.models import Okres, Narzedzia, Pomysl, Blad, Tradycja, Propozycja
from django.forms.widgets import Textarea, HiddenInput
from widgets import StarsRateWidget
from captcha.fields import CaptchaField


class NarzedzieForm(forms.Form):
    narzedzie = forms.ModelChoiceField(queryset=Okres.objects.all(), empty_label=None)
    nazwa = forms.CharField()
    opis = forms.CharField(widget=Textarea)

class RejestracjaForm(forms.Form):
    username = forms.CharField(label=u'Login')
    imie = forms.CharField(label=u'Imię')
    nazwisko = forms.CharField(label=u'Nazwisko')
    mail = forms.EmailField(label=u'E-mail')
    password = forms.CharField(widget=forms.PasswordInput(), label=u'Hasło')
    password2 = forms.CharField(widget=forms.PasswordInput(), label=u'Powtórz hasło')
    captcha = CaptchaField()

    def clean_password2(self):
        print self.cleaned_data
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password != password2:
            raise forms.ValidationError(u'Hasła nie są takie same!')

class PropozycjaForm(forms.Form):
    MODEL = (
        ('', ''),
        ('Pomysł', 'Pomysł nowego narzędzia'),
        ('Tradycja', 'Tradycję związaną z istniejącym narzędziem'),
        ('Błąd', 'Błąd związany z istniejącym narzędziem'),


    )
    model = forms.ChoiceField(choices=MODEL, label='Dodaj')
    narzedzie = forms.ModelChoiceField(queryset=Narzedzia.objects.all(), empty_label='Chcę zaproponować nowy',
                                       label='Narzędzie metodyczne', required=False)
    narzedzie_okres = forms.ModelChoiceField(queryset=Okres.objects.all(), empty_label=None,
                                             label='Okres którego dotyczy narzędzie', required=False)
    narzedzie_nazwa = forms.CharField(label='Nazwa narzędzia', required=False)
    narzedzie_opis = forms.CharField(widget=Textarea, label='Opis narzędzia', required=False)
    nazwa = forms.CharField(label='Nazwa propozycji')
    druzyna = forms.CharField(label='Nazwa dużyny')
    opis = forms.CharField(widget=Textarea, label='Opis propozycji')
    autor_prompt = forms.BooleanField(label='Ty jesteś autorem propozycji', initial=True, required=False)
    _autor = forms.CharField(label='Autor propozycji', required=False)


class KomentarzForm(forms.Form):
    RATING_CHOICES = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5),)
    propozycja = forms.ModelChoiceField(queryset=Propozycja.objects.all(), empty_label=None, widget=HiddenInput)
    zawartosc = forms.CharField(widget=Textarea, label=u'Zawartość')
    ocena = forms.IntegerField(widget=StarsRateWidget())

    def clean_ocena(self):
        error = forms.ValidationError(u'Ocena powinna byc liczbą całkowitą z przedziału od 0 do 5')
        data = self.cleaned_data['ocena']
        try:
            ocena = int(data)
        except ValueError:
            raise error
        if not (0 < ocena <= 5):
            raise error
        return ocena

    def __init__(self, *args, **kwargs):
        try:
            prop = kwargs.pop('propozycja')
            super(KomentarzForm, self).__init__(*args, **kwargs)
            self.fields['propozycja'].initial = prop
        except KeyError:
            super(KomentarzForm, self).__init__(*args, **kwargs)

