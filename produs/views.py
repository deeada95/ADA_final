from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, TemplateView
from .forms import FilterProductsForm, ContactForm
from .models import Produs, Favorite, ContactMessage


def index(request):
    return render(request, 'home.html')

class ProduseView(ListView):
    model = Produs
    template_name = 'produse.html'
    context_object_name = 'produse'

    def get_queryset(self):
        categorie_filtru = self.request.GET.get('categorie')
        queryset = Produs.objects.all()
        if categorie_filtru:
            queryset = queryset.filter(category_id = categorie_filtru)

        return queryset

    def get_context_data(self):
        context = super().get_context_data()
        context['form'] = FilterProductsForm(self.request.GET)
        return context

class DespreNoi(TemplateView):
    template_name = 'despre_noi.html'

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            nume = form.cleaned_data['nume']
            email = form.cleaned_data['email']
            mesaj = form.cleaned_data['mesaj']


            contact_message = ContactMessage(nume=nume, email=email, mesaj=mesaj)
            contact_message.save()

            return render(request, 'contact_succes.html', {'name': nume})
        else:
            print(form.errors)
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})
def produs_detalii(request, produs_id):
    produs = get_object_or_404(Produs, id=produs_id)
    imagini_produs = produs.imagini.all()
    favorite = Favorite.objects.filter(product= produs).filter(user=request.user)
    context = {
        'produs': produs,
        'imagini_produs': imagini_produs,
        'favorite': favorite
    }
    return render(request, 'produs_detalii.html', context)

def cauta_produs(request):
    query = request.GET.get('q', '')
    produse = Produs.objects.filter(nume__icontains = query)
    context = {
        'produse':produse,
        'query': query
    }
    return render(request, 'cauta_produs.html', context)

@login_required
def add_to_favorites(request, product_id):
    product = get_object_or_404(Produs, id=product_id)
    favorite, created = Favorite.objects.get_or_create(user=request.user, product=product)

    if not created:
        favorite.delete()
        return JsonResponse({"message": "Produs eliminat din favorite", "status": "removed"})

    return JsonResponse({"message": "Produs adăugat la favorite", "status": "added"})

@login_required
def favorites_list(request):
    favorites = Favorite.objects.filter(user=request.user)
    return render(request, "favorites_list.html", {"favorites": favorites})