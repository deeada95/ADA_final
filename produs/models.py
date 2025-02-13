from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE


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
    descriere = models.TextField(blank=True, null=True)
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

class ContactMessage(models.Model):
    nume = models.CharField(max_length=100)
    email = models.EmailField()
    mesaj = models.TextField()


    def __str__(self):
        return f"Mesaj de la {self.nume} - {self.email}"

class CosCumparaturi(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    produs = models.ForeignKey(Produs, on_delete=CASCADE)
    cantitate = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ('user', 'produs')

    def __str__(self):
        return f"{self.user.username} - {self.produs.nume} (x{self.cantitate})"

class Comanda(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'În așteptare'),
        ('Processing', 'În procesare'),
        ('Shipped', 'Expediată'),
        ('Delivered', 'Livrată'),
        ('Cancelled', 'Anulată'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    produse = models.ManyToManyField(Produs, through='ComandaFinala')
    data_creare = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    total = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Comanda #{self.id} - {self.user.username} - {self.status}"

class ComandaFinala(models.Model):
    comanda = models.ForeignKey(Comanda, on_delete=models.CASCADE)
    produs = models.ForeignKey(Produs, on_delete=models.CASCADE)
    cantitate = models.PositiveIntegerField(default=1)
    pret_unitar = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.produs.nume} - {self.cantitate}"
