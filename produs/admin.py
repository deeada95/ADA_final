from django.contrib import admin
from produs.models import Produs, Category, ImaginiProdus, Favorite, ContactMessage

# Register your models here.

admin.site.register(Category)
admin.site.register(Produs)
admin.site.register(ImaginiProdus)
admin.site.register(Favorite)
admin.site.register(ContactMessage)

