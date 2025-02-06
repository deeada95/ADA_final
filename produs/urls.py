from django.urls import path
from django.views.generic import TemplateView
from . import views
from .views import ProduseView, index

urlpatterns = [
    path('', index, name = 'home'),
    path('produse/', ProduseView.as_view(), name='produse'),
    path('produs/<int:produs_id>/', views.produs_detalii, name='produs_detalii'),
    path('despre noi/', TemplateView.as_view(template_name='despre_noi.html'), name='despre_noi'),
    path('program-contact/', TemplateView.as_view(template_name='program_contact.html'), name='program_contact'),
    path('cauta_produs/', views.cauta_produs, name='cauta_produs')

    ]