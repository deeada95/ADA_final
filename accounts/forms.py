from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db.transaction import atomic
from accounts.models import Profil



class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    telefon = forms.CharField(max_length=15, required=True)
    data_nasterii = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=True)

class Meta(UserCreationForm.Meta):
        fields = ['username', 'email', 'telefon', 'data_nasterii','password1','password2']

@atomic
def save(self, commit=True):
    user = super().save(commit=False)
    if commit:
        user.save()

    profil = Profil(
        user=user,
        telefon=self.cleaned_data['telefon'],
        data_nasterii=self.cleaned_data['data_nasterii']
    )
    profil.save()


    return user

