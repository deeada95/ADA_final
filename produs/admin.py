from django.contrib import admin

from produs.models import Produs, Client, Comanda

# Register your models here.
admin.site.register(Produs)
admin.site.register(Client)
admin.site.register(Comanda)