"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from CTGerson import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name = 'home'),
    url(r'^lista_onibus/$', views.bus_list, name = 'bus_list'),
    url(r'^editar_onibus/(?P<pk>[0-9]+)/$', views.edit_bus, name='edit_bus'),
    url(r'^remover_onibus/(?P<pk>[0-9]+)/$', views.remove_bus, name = 'remove_bus'),
    url(r'^cadastrar_onibus/$', views.register_bus, name = 'register_bus'),
]
