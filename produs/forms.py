from django import forms
from produs.models import Category


class FilterProductsForm(forms.Form):
    categorie = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label="Filtreaza",
        required=False,
        widget=forms.Select(attrs={"class": "form-control"})
    )

class ContactForm(forms.Form):
    name = forms.CharField(label="Numele tău", max_length=100)
    email = forms.EmailField(label="Email-ul tău")
    message = forms.CharField(label="Mesajul tău", widget=forms.Textarea)

