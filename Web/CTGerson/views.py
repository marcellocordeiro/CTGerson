from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Bus
from .forms import BusForm

def login(request):
    return render(request, 'login.html', {})

def bus_list(request):
    buses = Bus.objects.all()
    return render(request, 'bus_list.html', {'buses': buses})

def register_bus(request):
    if request.method == "POST":
        form = BusForm(request.POST)
        if form.is_valid():
            bus = form.save()
            return redirect('bus_list')
    else:
        form = BusForm()
    return render(request, 'register_bus.html', {'form': form})


#def bus(request):

    #return render()