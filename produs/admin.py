from django.contrib import admin
from produs.models import Produs, Category, ImaginiProdus, Favorite, ContactMessage, Comanda, ComandaFinala, \
    CosCumparaturi

# Register your models here.

admin.site.register(Category)
admin.site.register(Produs)
admin.site.register(ImaginiProdus)
admin.site.register(Favorite)
admin.site.register(ContactMessage)
admin.site.register(Comanda)
admin.site.register(CosCumparaturi)
admin.site.register(ComandaFinala)

