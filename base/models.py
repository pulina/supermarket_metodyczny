# -*- coding: UTF-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from orderable.models import Orderable
from polymorphic.polymorphic_model import PolymorphicModel
from django.db.models import Avg


class Narzedzia(models.Model):
    nazwa = models.CharField(max_length=200)
    opis = models.TextField()
    autor = models.ForeignKey(User)


    class Meta:
        verbose_name = 'Narzędzie'
        verbose_name_plural = 'Narzędzia'

    def __unicode__(self):
        return self.nazwa

    def get_absolute_url(self):
        return reverse('narzedzia', args=[self.id])


class Rok(Orderable):
    nazwa = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nazwa

    class Meta(Orderable.Meta):
        verbose_name_plural = 'Lata'

class Okres(Orderable):
    nazwa = models.CharField(max_length=200)
    opis = models.TextField()
    rok = models.ForeignKey(Rok)
    narzedzia = models.ManyToManyField(Narzedzia, blank=True, null=True)

    class Meta(Orderable.Meta):
        verbose_name_plural = 'Okresy'

    def __unicode__(self):
        return u'{} {}'.format(self.nazwa, self.rok)

class Propozycja(PolymorphicModel):
    nazwa = models.CharField(max_length=200)
    druzyna = models.CharField(max_length=200)
    dodana_przez = models.ForeignKey(User)
    opis = models.TextField()
    narzedzie = models.ManyToManyField(Narzedzia)

    def __unicode__(self):
        return self.nazwa

class Blad(Propozycja):

    class Meta:
        verbose_name = 'Błąd'
        verbose_name_plural = 'Błędy'

    def get_absolute_url(self):
        return reverse('blad', args=[self.id])

class Tradycja(Propozycja):

    class Meta:
        verbose_name_plural = 'Tradycje'

    def get_absolute_url(self):
        return reverse('tradycja', args=[self.id])

class Pomysl(Propozycja):
    zaakceptowany = models.BooleanField()

    @property
    def rate(self):
        # TODO: optymalize - on comment save calculate new rate for pomysl obj and store it in db this will allow us to get top_rated with single query
        return Komentarz.objects.filter(pomysl=self).aggregate(Avg('ocena'))['ocena__avg']


    class Meta:
        verbose_name = 'Pomysł'
        verbose_name_plural = 'Pomysły'

    def get_absolute_url(self):
        return reverse('pomysl', args=[self.id])


class Komentarz(models.Model):
    autor = models.ForeignKey(User)
    zawartosc = models.TextField()
    data_publikacji = models.DateTimeField('data publikacji')
    pomysl = models.ForeignKey(Pomysl)
    ocena = models.IntegerField()

    class Meta:
        verbose_name = 'Komentarz'
        verbose_name_plural = 'Komentarze'

    def __unicode__(self):
        return u'{0} - {1}'.format(self.autor.username, self.zawartosc)
