"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include, re_path
from CTGerson import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('ajax/update_data/', views.update_data, name='update_data'),
    path('ajax/update_location/', views.update_location, name='update_location'),
    path('', views.home, name='home'),
    path('lista_onibus/', views.bus_list, name='bus_list'),
    path('cadastrar_onibus/', views.register_bus, name = 'register_bus'),
    re_path('editar_onibus/(?P<pk>[0-9]+)/', views.edit_bus, name='edit_bus'),
    re_path('remover_onibus/(?P<pk>[0-9]+)/', views.remove_bus, name = 'remove_bus'),
    re_path('onibus/(?P<pk>[0-9]+)/', views.bus_detail, name='bus_detail'),
    path('salvar_ocorrencia/', views.update_occurrence, name='update_occurrence'),
    path('lista_ocorrencias/', views.occurrences_list, name='occurrences_list'),
    path('ocorrencia/', views.occurrence, name='occurrence'),
    path('reject_alert/', views.reject_alert, name='reject_alert'),
    path('get_officer_location/<lat>/<long>', views.get_officer_location, name='get_officer_location')
]
