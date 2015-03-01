# -*- coding: UTF-8 -*-
from django.db import models
from django.contrib.auth.models import User, Group
from django.core.urlresolvers import reverse
from orderable.models import Orderable
from polymorphic.polymorphic_model import PolymorphicModel
from django.db.models import Avg


class Narzedzia(models.Model):
    nazwa = models.CharField(max_length=200)
    opis = models.TextField()
    dodana_przez = models.ForeignKey(User)
    _autor = models.CharField(max_length=255, blank=True, null=True)
    zaakceptowany = models.BooleanField(default=False)


    class Meta:
        verbose_name = 'Narzędzie'
        verbose_name_plural = 'Narzędzia'

    def __unicode__(self):
        return self.nazwa

    def get_absolute_url(self):
        return reverse('narzedzia', args=[self.id])

    @property
    def autor(self):
        return self._autor or self.dodana_przez.get_full_name

    @autor.setter
    def autor_setter(self, value):
        # XXX: Does not save obj
        if isinstance(User, value):
            self.dodana_przez = value
        else:
            self._autor = value


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
    druzyna = models.CharField(max_length=200, blank=True, null=True)
    dodana_przez = models.ForeignKey(User)
    _autor = models.CharField(max_length=255, blank=True, null=True)
    opis = models.TextField()
    narzedzie = models.ForeignKey(Narzedzia)
    zaakceptowany = models.BooleanField(default=False)
    moment_wystapienia = models.CharField(max_length=200, blank=True, null=True)

    def __unicode__(self):
        return self.nazwa

    @property
    def autor(self):
        return self._autor or self.dodana_przez.get_full_name

    @autor.setter
    def autor_setter(self, value):
        # XXX: Does not save obj
        if isinstance(User, value):
            self.dodana_przez = value
        else:
            self._autor = value


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
    @property
    def rate(self):
        # TODO: optymalize - on comment save calculate new rate for pomysl obj and store it in db this will allow us to get top_rated with single query
        return Komentarz.objects.filter(propozycja=self).aggregate(Avg('ocena'))['ocena__avg'] or u'Brak'

    @property
    def rate_prof(self):
        # TODO: optymalize - on comment save calculate new rate for pomysl obj and store it in db this will allow us to get top_rated with single query
        return  Komentarz.objects.filter(propozycja=self,
                                     autor__groups__name="Edytor").aggregate(
                Avg('ocena'))['ocena__avg'] or u'Brak'


    class Meta:
        verbose_name = 'Pomysł'
        verbose_name_plural = 'Pomysły'

    def get_absolute_url(self):
        return reverse('pomysl', args=[self.id])


class Komentarz(models.Model):
    autor = models.ForeignKey(User)
    zawartosc = models.TextField()
    data_publikacji = models.DateTimeField('data publikacji')
    propozycja = models.ForeignKey(Propozycja)
    ocena = models.IntegerField()

    class Meta:
        verbose_name = 'Komentarz'
        verbose_name_plural = 'Komentarze'

    def __unicode__(self):
        return u'{0} - {1}'.format(self.autor.username, self.zawartosc)
