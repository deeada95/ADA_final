"""
URL configuration for farmacie_online project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path
from django.views.generic import TemplateView
from accounts.views import CustomLoginView, CustomPasswordChangeView, SignUpView
from produs import views
from produs.views import index, ProduseView, add_to_favorites, favorites_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name = 'home'),
    path('produse/', ProduseView.as_view(), name='produse'),
    path('produs/<int:produs_id>/', views.produs_detalii, name='produs_detalii'),
    path('despre noi/', TemplateView.as_view(template_name='despre_noi.html'), name='despre_noi'),
    path('contact/', views.contact, name='contact'),
    path('contact/success/', TemplateView.as_view(template_name='contact_success.html'), name='contact_success'),
    path('cauta_produs/', views.cauta_produs, name='cauta_produs'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('schimbare_parola/', CustomPasswordChangeView.as_view(), name='schimbare_parola'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('favorite/<int:product_id>/', add_to_favorites, name='add_to_favorites'),
    path('favorites_list/', favorites_list, name='favorites_list'),


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

