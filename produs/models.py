from datetime import datetime

from django.conf import settings
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Produs(models.Model):
    nume = models.CharField(max_length=100)
    descriere = models.TextField()
    pret = models.DecimalField(max_digits=6, decimal_places=2)
    imagine = models.ImageField(upload_to='produse/', blank = True, null= True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="produse",default=1)
    def __str__(self):
        return self.nume
class ImaginiProdus(models.Model):
    produs = models.ForeignKey(Produs, related_name='imagini', on_delete=CASCADE)
    imagine = models.ImageField(upload_to='produse_imagini', null=False, default ='media/produse_imagini_suplimentare')
    def __str__(self):
        return self.produs.nume


