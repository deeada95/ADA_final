
from django.contrib.auth import login, authenticate
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from produs.forms import RegisterForm, CustomLoginForm
from produs.models import Produs

def index(request):
    return render(request, 'home.html')

def posts_view(request):
    posts = Produs.objects.all()
def produse(request):
    produse = Produs.objects.all()
    return render(request, 'produse.html', {'produse': produse})
def despre_noi(request):
    return render(request, 'despre_noi.html')
def program_contact(request):
    return render(request, 'program_contact.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('produse')
    else:
        form = RegisterForm()
    return render(request, 'register.html',{'form':form})

def signin(request):
    user = None

    if request.method == 'POST':
        form = CustomLoginForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'signin.html', {'form': form, 'error': 'Autentificare eșuată!'})
    else:
        form = CustomLoginForm()
    return render(request, 'signin.html', {'form': form})


