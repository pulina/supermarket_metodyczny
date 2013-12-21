# -*- coding: UTF-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from orderable.models import Orderable


SZKODLIWOSC = (
    ('vh', 'bardzo wysoka'),
    ('h', 'wysoka'),
    ('m', 'umiarkowana'),
    ('l', 'niska')
)
STOPNIE = (
    ('bs', u'Bez stopnia'),
    ('ml', u'Młodzik/Ochotniczka'),
    ('wyw', u'Wywiadowca/Tropicielka'),
    ('cw', u'Śamerytanka/Ćwik'),
    ('ho', u'Harcerz Orli/Wędrowniczka'),
    ('hr', u'Harcerz/Harcerka Rzeczypospolitej')
)
    

class Poropozycja(models.Model):
    """
    Why charField for choice option like 'funkcja' ... a lot of my change
    no sense to prepere choice option.
    """
    n="Niewiadomo"
    nick = models.CharField(max_length=200,default=n)
    email = models.EmailField(max_length=200,default=n)
    stopien_instruktorski = models.CharField(max_length=200,default=n)
    funkcja = models.CharField(max_length=200,default=n)
    plec = models.CharField(max_length=200,default=n)
    organizacja = models.CharField(max_length=200,default=n)
    skad_jestes = models.CharField(max_length=200,default=n)
    propozycja_dotyczy = models.CharField(max_length=200,default=n)
    opis_problemu = models.TextField()


class Funkcja(models.Model):
    nazwa = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Funkcje'

    def __unicode__(self):
        return self.nazwa


class Forma(models.Model):
    nazwa = models.CharField(max_length=200)
    dodana_przez = models.CharField(max_length=200,default="System")
    opis = models.TextField()

    class Meta:
        verbose_name_plural = 'Formy'

    def __unicode__(self):
        return self.nazwa

    def get_absolute_url(self):
        return reverse('forma', args=[self.id])


class Okres(Orderable):
    nazwa = models.CharField(max_length=200)
    opis = models.TextField()
    wiek_min = models.IntegerField()
    wiek_max = models.IntegerField()
    stopien = models.CharField(max_length=200, choices=STOPNIE)
    funkcja = models.ManyToManyField(Funkcja, blank=True, null=True)
    forma = models.ManyToManyField(Forma, blank=True, null=True)

    class Meta(Orderable.Meta):
        verbose_name_plural = 'Okresy'

    def __unicode__(self):
        return self.nazwa


class Blad(models.Model):
    nazwa = models.CharField(max_length=200)
    opis = models.TextField()
    szkodliwosc = models.CharField(max_length=200, choices=SZKODLIWOSC)
    dodana_przez = models.CharField(max_length=200,default="System")


    class Meta:
        verbose_name = 'Błąd'
        verbose_name_plural = 'Błędy'

    def __unicode__(self):
        return self.nazwa

    def get_absolute_url(self):
        return reverse('blad', args=[self.id])


class Tradycja(models.Model):
    nazwa = models.CharField(max_length=200)
    opis = models.TextField()
    dodana_przez = models.CharField(max_length=200,default="System")


    class Meta:
        verbose_name_plural = 'Tradycje'

    def __unicode__(self):
        return self.nazwa

    def get_absolute_url(self):
        return reverse('tradycja', args=[self.id])


class Pomysl(models.Model):
    nazwa = models.CharField(max_length=200)
    zgodnosc_z_metoda = models.BooleanField()
    skutecznosc_base = models.IntegerField()
    opis = models.TextField()
    blady = models.ManyToManyField(Blad, blank=True, null=True)
    zaakceptowany = models.BooleanField()
    forma = models.ManyToManyField(Forma, blank=True, null=True)
    tradycja = models.ManyToManyField(Tradycja, blank=True, null=True)
    dodana_przez = models.CharField(max_length=200,default="System")

    class Meta:
        verbose_name = 'Pomysł'
        verbose_name_plural = 'Pomysły'

    def __unicode__(self):
        return self.nazwa

    def get_absolute_url(self):
        return reverse('pomysl', args=[self.id])


class Komentarz(models.Model):
    autor = models.ForeignKey(User)
    zawartosc = models.CharField(max_length=200)
    data_publikacji = models.DateTimeField('data publikacji')
    pomysl = models.ForeignKey(Pomysl)
    ocena = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Komentarze'

    def __unicode__(self):
        return '{0} - {1}'.format(self.autor.username, self.zawartosc)
