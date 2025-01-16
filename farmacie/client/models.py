from django.db import models

class Client(models.Model):
    prenume = models.CharField(max_length=100)
    nume = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefon = models.CharField(max_length=10)
    adresa = models.TextField()
    def __str__(self):
        return f'{self.prenume} {self.nume}'
# Create your models here.
