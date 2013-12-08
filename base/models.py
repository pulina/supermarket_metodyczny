# -*- coding: UTF-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes import generic

SZKODLIWOSC = (
    ('vh', 'bardzo wysoka'),
    ('h', 'wysoka'),
    ('m', 'umiarkowana'),
    ('l', 'niska')
)
TAKNIE = (
    ('True', 'Tak'),
    ('False', 'Nie'),
)
STOPNIE = (
    ('bs', u'Bez stopnia'),
    ('ml', u'Młodzik/Ochotniczka'),
    ('wyw', u'Wywiadowca/Tropicielka'),
    ('cw', u'Śamerytanka/Ćwik'),
    ('ho', u'Harcerz Orli/Wędrowniczka'),
    ('hr', u'Harcerz/Harcerka Rzeczypospolitej')
)


class Funkcja(models.Model):
    nazwa = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nazwa


class Forma(models.Model):
    nazwa = models.CharField(max_length=200)
    wiek_min = models.IntegerField()
    wiek_max = models.IntegerField()

    def __unicode__(self):
        return self.nazwa


class Okres(models.Model):
    generic_position = generic.GenericRelation('generic_positions.ObjectPosition')
    nazwa = models.CharField(max_length=200)
    opis = models.CharField(max_length=200)
    wiek_min = models.IntegerField()
    wiek_max = models.IntegerField()
    stopien = models.CharField(max_length=200, choices=STOPNIE)
    funkcja = models.ManyToManyField(Funkcja, blank=True, null=True)
    forma = models.ManyToManyField(Forma, blank=True, null=True)

    def __unicode__(self):
        return self.nazwa


class Blad(models.Model):
    nazwa = models.CharField(max_length=200)
    opis = models.CharField(max_length=200)
    szkodliwosc = models.CharField(max_length=200, choices=SZKODLIWOSC)

    def __unicode__(self):
        return self.nazwa


class Tradycja(models.Model):
    opis = models.CharField(max_length=200)
    nazwa = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nazwa


class Pomysl(models.Model):
    nazwa = models.CharField(max_length=200)
    zgodnosc_z_metoda = models.CharField(max_length=5, choices=TAKNIE)
    skutecznosc_base = models.IntegerField()
    opis = models.CharField(max_length=200)
    blady = models.ManyToManyField(Blad, blank=True, null=True)
    zaakceptowany = models.BooleanField()
    forma = models.ManyToManyField(Forma, blank=True, null=True)
    tradycja = models.ManyToManyField(Tradycja, blank=True, null=True)

    def __unicode__(self):
        return self.nazwa


class Komentarz(models.Model):
    autor = models.ForeignKey(User)
    zawartosc = models.CharField(max_length=200)
    data_publikacji = models.DateTimeField('data publikacji')
    pomysl = models.ForeignKey(Pomysl)
    ocena = models.IntegerField()

    def __unicode__(self):
        return '{0} - {1}'.format(self.autor.username, self.zawartosc)
