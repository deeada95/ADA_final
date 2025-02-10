from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Category(models.Model):
    nume = models.CharField(max_length=100)
    descriere = models.TextField(blank=True)

    def __str__(self):
        return self.nume
    def __str__(self):
        return f"{self.nume}"

class Produs(models.Model):
    nume = models.CharField(max_length=100)
    descriere = models.TextField()
    pret = models.DecimalField(max_digits=6, decimal_places=2)
    imagine = models.ImageField(upload_to='produse/', blank = True, null= True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="produse",default=1)

    def __str__(self):
        return self.nume
class ImaginiProdus(models.Model):
    produs = models.ForeignKey(Produs, related_name='imagini', on_delete=models.CASCADE)
    imagine = models.ImageField(upload_to='produse_imagini')
    def __str__(self):
        return self.produs.nume

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Produs, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'product')

    def __str__(self):
        return f"{self.user.username} - {self.product.nume}"
