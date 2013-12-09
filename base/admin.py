from django.contrib import admin
from base.models import Blad, Pomysl, Komentarz, Tradycja, Forma, Okres, Funkcja
from orderable.admin import OrderableAdmin

admin.site.register(Blad)
admin.site.register(Pomysl)
admin.site.register(Komentarz)
admin.site.register(Tradycja)
admin.site.register(Forma)
admin.site.register(Funkcja)


class okresAdmin(OrderableAdmin):
    list_display = ('sort_order_display', '__str__')

    class Media:
        js = ('http://ajax.googleapis.com/ajax/libs/jqueryui/1.9.2/jquery-ui.js',)

admin.site.register(Okres, okresAdmin)
