from django import forms
from produs.models import Category

class FilterProductsForm(forms.Form):
    categorie = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label="Filtreaza",
        widget=forms.Select(attrs={"class": "form-control"})
    )