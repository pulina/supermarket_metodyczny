from django.contrib import admin
from base.models import Blad, Pomysl, Komentarz, Tradycja, Forma, Okres, Funkcja
from orderable.admin import OrderableAdmin


class MyAdmin(admin.ModelAdmin):
    class Media:
        css = {
            "all": ("admin_styles.css",)
        }

admin.site.register(Blad)
admin.site.register(Pomysl)
admin.site.register(Komentarz)
admin.site.register(Tradycja)
admin.site.register(Forma)
admin.site.register(Funkcja)


class okresAdmin(OrderableAdmin, MyAdmin):
    list_display = ('sort_order_display', '__str__')
    list_display_links = ('__str__',)
    readonly_fields = ('sort_order',)

    class Media:
        js = ('http://ajax.googleapis.com/ajax/libs/jqueryui/1.9.2/jquery-ui.js',)

admin.site.register(Okres, okresAdmin)
