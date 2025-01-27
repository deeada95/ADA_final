from datetime import datetime
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