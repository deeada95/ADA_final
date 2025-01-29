from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User

from .models import Client


class RegisterForm(UserCreationForm):

    email= forms.EmailField(label='Email')
    password1 = forms.CharField(widget=forms.PasswordInput, label='Parola')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirma parola')

    prenume = forms.CharField(max_length=100, label='Prenume')
    nume = forms.CharField(max_length=100, label='Nume')
    telefon = forms.CharField(max_length=10, label='Telefon')
    adresa = forms.CharField(max_length=200 , label='Adresă')

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']

    def save(self, commit=True):
        user= super().save(commit=False)
        user.username = self.cleaned_data['email']
        if commit:
            user.set_password(self.cleaned_data['password1'])
            user.save()

        client= Client(
            prenume= self.cleaned_data['prenume'],
            nume= self.cleaned_data['nume'],
            email = self.cleaned_data['email'],
            telefon = self.cleaned_data['telefon'],
            adresa = self.cleaned_data['adresa']
        )
        client.save()
        return user

class CustomLoginForm(AuthenticationForm):
    username = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput, label='Parola')
