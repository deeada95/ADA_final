from django.db import models
class Produs(models.Model):
    nume = models.CharField(max_length=100)
    descriere = models.TextField()
    pret = models.DecimalField(max_digits=6, decimal_places=2)
    def __str__(self):
        return self.nume
# Create your models here.
