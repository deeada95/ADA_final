from datetime import datetime

from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from django.db import models

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

class Client(models.Model):

    prenume = models.CharField(max_length=100)
    nume = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    telefon = models.CharField(max_length=10)
    adresa = models.TextField()

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return f'{self.prenume} {self.nume}'

class Comanda(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, default=1)
    produse = models.ManyToManyField(Produs)
    data_creare = models.DateTimeField(default=datetime.now())
    status = models.CharField(
        max_length=20,
        choices=[
            ('in asteptare', 'În așteptare'),
            ('procesata', 'Procesată'),
            ('livrata', 'Livrată'),
            ('anulata', 'Anulată'),
        ],
        default='in asteptare',
    )

    def __str__(self):
        return f'Comanda #{self.id} - {self.client}'