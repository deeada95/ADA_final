from django.contrib import admin

from produs.models import Produs, Client, Comanda, Category
# Register your models here.
admin.site.register(Category)
admin.site.register(Produs)
admin.site.register(Client)
admin.site.register(Comanda)
