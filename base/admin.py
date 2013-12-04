from django.contrib import admin
from base.models import Blad, Pomysl, Komentarz, Tradycja, Forma, Okres, Funkcja 
from generic_positions.admin import GenericPositionsAdmin

admin.site.register(Blad)
admin.site.register(Pomysl)
admin.site.register(Komentarz)
admin.site.register(Tradycja)
admin.site.register(Forma)
admin.site.register(Funkcja)
admin.site.register(Okres, GenericPositionsAdmin)
