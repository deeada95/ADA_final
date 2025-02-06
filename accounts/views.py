from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from accounts.forms import SignUpForm


# Create your views here.
class CustomLoginView(LoginView):
    template_name = 'login.html'
class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'schimbare_parola.html'
    form_class = SignUpForm
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

