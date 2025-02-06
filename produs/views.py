from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, TemplateView

from .forms import FilterProductsForm
from .models import Produs

def index(request):
    return render(request, 'home.html')

class ProduseView(ListView):
    model = Produs
    template_name = 'produse.html'
    context_object_name = 'produse'
    paginate_by = 5
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

class Program(TemplateView):
    template_name = 'program_contact.html'

def produs_detalii(request, produs_id):
    produs = get_object_or_404(Produs, id=produs_id)
    imagini_produs = produs.imagini.all()
    context = {
        'produs': produs,
        'imagini_produs': imagini_produs
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