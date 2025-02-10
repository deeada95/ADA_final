from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE, ForeignKey


# Create your models here.

class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    telefon = models.CharField(max_length=15)
    adresa = models.CharField(max_length=255)
    data_nasterii = models.DateField()
    def __str__(self):
        return self.user.username

class UserPostRelation(models.Model):
    user = ForeignKey(User, on_delete=CASCADE)
    def __str__(self):
        return self.user.username
