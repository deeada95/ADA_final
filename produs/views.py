from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, TemplateView
from .forms import FilterProductsForm, ContactForm
from .models import Produs, Favorite, ContactMessage, Comanda, ComandaFinala, CosCumparaturi


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
    favorite = None
    in_cos = False

    if request.user.is_authenticated:
        favorite = Favorite.objects.filter(product=produs, user=request.user)
        in_cos= CosCumparaturi.objects.filter(user=request.user, produs=produs).exists()

    context = {
        'produs': produs,
        'imagini_produs': imagini_produs,
        'favorite': favorite,
        'in_cos': in_cos

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

@login_required (login_url='/accounts/login/')
def adauga_in_cos(request, produs_id):
    produs = get_object_or_404(Produs, id=produs_id)
    produse_cos, created = CosCumparaturi.objects.get_or_create(user=request.user, produs=produs)

    if not created:
        produse_cos.cantitate += 1
        produse_cos.save()

    return redirect('vizualizare_cos')

@login_required
def vizualizare_cos(request):
    produse_cos = CosCumparaturi.objects.filter(user=request.user)
    total = sum(item.produs.pret * item.cantitate for item in produse_cos)

    return render(request, 'cos_cumparaturi.html', {'produse_cos': produse_cos, 'total': total})
@login_required
def elimina_din_cos(request, cos_id):
    produse_cos = get_object_or_404(CosCumparaturi, id=cos_id, user=request.user)
    produse_cos.delete()
    return redirect('vizualizare_cos')

@login_required
def finalizare_comanda(request):
    produse_cos = CosCumparaturi.objects.filter(user=request.user)

    if not produse_cos.exists():
        messages.error(request, "Nu aveți produse în coș!")
        return redirect('vizualizare_cos')

    total = sum(item.produs.pret * item.cantitate for item in produse_cos)
    comanda = Comanda.objects.create(user=request.user, total=total)

    for item in produse_cos:
        ComandaFinala.objects.create(
            comanda=comanda,
            produs=item.produs,
            cantitate=item.cantitate,
            pret_unitar=item.produs.pret)

    produse_cos.delete()
    messages.success(request, "Comanda a fost plasată cu succes!")
    return render(request, 'comanda_plasata.html', {'comanda': comanda})