from django.db import models

# Create your models here.
class Produs(models.Model):
    nume = models.CharField(max_length=100)
    descriere = models.TextField()
    pret = models.DecimalField(max_digits=6, decimal_places=2)
    def __str__(self):
        return self.nume

class Client(models.Model):
    prenume = models.CharField(max_length=100)
    nume = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefon = models.CharField(max_length=10)
    adresa = models.TextField()
    def __str__(self):
        return f'{self.prenume} {self.nume}'