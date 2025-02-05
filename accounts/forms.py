from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    telefon = forms.CharField(max_length=15, required=False)
    email = forms.EmailField(required=True)
    adresa = forms.CharField(max_length=200, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2','telefon']

class LoginForm(AuthenticationForm):
    pass


class RegisterForm:
    pass