from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from produs.models import Produs

def index(request):
    return render(request, 'home.html')
def despre_noi(request):
    return render(request, 'despre_noi.html')
def program_contact(request):
    return render(request, 'program_contact.html')

