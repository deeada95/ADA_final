from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView
from accounts.forms import SignUpForm
from accounts.models import UserPostRelation
from produs.models import Comanda, ComandaFinala


# Create your views here.
class CustomLoginView(LoginView):
    template_name = 'login.html'
class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'schimbare_parola.html'
    success_url = reverse_lazy('home')

class SignUpView(CreateView):
    template_name = 'signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('home')
@login_required
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def favourites_view(request):
    posts = UserPostRelation.objects.filter(user=request.user)
    return render(
        request,
        'favorites_list.html',
        context={'posts': posts}
    )
def vizualizare_comanda(request):
    comenzi = Comanda.objects.filter(user=request.user)
    return render(request, 'vizualizare_comenzi.html', {'comenzi': comenzi})

@login_required
def detalii_comanda(request, comanda_id):
    comanda = get_object_or_404(Comanda, id=comanda_id, user=request.user)
    comanda_finala = ComandaFinala.objects.filter(comanda=comanda)

    return render(request, 'detalii_comanda.html', {'comanda': comanda, 'comanda_finala': comanda_finala})
