# -*- coding: UTF-8 -*-
from django import forms
from base.models import Okres, Narzedzia, Pomysl, Blad, Tradycja, Propozycja, Post
from django.forms.widgets import Textarea, HiddenInput
from widgets import StarsRateWidget
from tinymce.widgets import TinyMCE
#from pygments.lexers.other import ModelicaLexer
from captcha.fields import CaptchaField


class NarzedzieForm(forms.ModelForm):
    class Meta:
        model = Narzedzia
        fields = ['nazwa', 'opis', '_autor' ]

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
        return password2

class PropozycjaForm(forms.Form):
    MODEL = (
        ('', ''),
        ('Pomysł', 'Pomysł nowego narzędzia'),
        ('Tradycja', 'Tradycję związaną z istniejącym narzędziem'),
        ('Błąd', 'Błąd związany z istniejącym narzędziem'),#


    )
    model = forms.ChoiceField(choices=MODEL, label='Dodaj')
    narzedzie = forms.ModelChoiceField(queryset=Narzedzia.objects.all(), empty_label='Chcę zaproponować nowy',
                                       label='Narzędzie metodyczne', required=False)
    narzedzie_okres = forms.ModelChoiceField(queryset=Okres.objects.all(), empty_label=None,
                                             label='Okres którego dotyczy narzędzie', required=False)
    narzedzie_nazwa = forms.CharField(label='Nazwa narzędzia', required=False)
    #w narzedziu zmienić z Textarea na TinyMCE
    narzedzie_opis = forms.CharField(widget=TinyMCE, label='Opis narzędzia', required=False)
    nazwa = forms.CharField(label='Nazwa propozycji')
    druzyna = forms.CharField(label='Nazwa dużyny', required=False)
    moment_wystapienia = forms.CharField(label='Moment wystąpienia', required=False)
    opis = forms.CharField(widget=Textarea, label='Opis propozycji')
    autor_prompt = forms.BooleanField(label='Ty jesteś autorem propozycji', initial=True, required=False)
    _autor = forms.CharField(label='Autor propozycji', required=False)

    def clean_druzyna(self):
        if self.cleaned_data['model'] != u'Błąd' and not self.cleaned_data['druzyna']:
            raise forms.ValidationError(u'Pole drużyna jest wymagane!')
        return self.cleaned_data['druzyna']


class KomentarzForm(forms.Form):
    RATING_CHOICES = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5),)
    propozycja = forms.ModelChoiceField(queryset=Propozycja.objects.all(), empty_label=None, widget=HiddenInput)
    zawartosc = forms.CharField(widget=TinyMCE, label=u'Zawartość')
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


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('Tytul', 'Tekst',) 
        widgets = {
            'Tekst': TinyMCE(attrs={'cols': 50, 'rows': 10}),
        }
        
        
#class PropozycjaForm(forms.ModelForm):
#    
#    class Meta:
#        MODEL = (
#            ('', ''),
#            ('Pomysł', 'Pomysł nowego narzędzia'),
#            ('Tradycja', 'Tradycję związaną z istniejącym narzędziem'),
#            ('Błąd', 'Błąd związany z istniejącym narzędziem'),
#        )
#        
#        model = None
#        fields = None
#        
#        def __init__(self):
#            MODEL = self.MODEL
#            if(self.MODEL == 'Pomysł'):
#                self.model = MODEL
#                self.fields = ('narzedzie_okres', 'narzedzie_nazwa', 'narzedzie_opis',)
#                
#            if(self.MODEL == 'Tradycja'):
#                self.model = MODEL
#                self.fields = ('nazwa', 'druzyna', 'moment_wystapienia', 'opis', 'autor_prompt', '__autor',)
#                
#            if(self.MODEL == 'Błąd'):
#                self.model = MODEL
#                self.fields = ('narzedzie_okres', 'narzedzie_nazwa', 'narzedzie_opis',)
#                
#        def clean_druzyna(self):
#            if self.cleaned_data['model'] != u'Błąd' and not self.cleaned_data['druzyna']:
#                raise forms.ValidationError(u'Pole drużyna jest wymagane!')
#            return self.cleaned_data['druzyna']
        
        