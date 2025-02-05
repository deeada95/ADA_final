from django.conf import settings
from django.db import models
from django.db.models import CASCADE


# Create your models here.

class Profil(models.Model):
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    telefon = models.CharField(max_length=15)
    adresa = models.CharField(max_length=255)
    data_nasterii = models.DateField()

    def __str__(self):
        return f"Profilul lui {self.utilizator.username}"
