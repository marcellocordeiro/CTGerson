from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Bus
from .forms import BusForm

def home(request):
    return render(request, 'home.html', {})

def bus_list(request):
    buses = Bus.objects.all()
    return render(request, 'bus_list.html', {'buses': buses})

def register_bus(request):
    if request.method == "POST":
        form = BusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bus_list')
    else:
        form = BusForm()
    return render(request, 'register_bus.html', {'form': form})

def edit_bus(request, pk):
    bus = get_object_or_404(Bus, pk = pk)

    if request.method == "POST":
        form = BusForm(request.POST, instance = bus)
        if form.is_valid():
            form.save()
            return redirect('bus_list')
    else:
        form = BusForm(instance = bus)

    return render(request, 'edit_bus.html', {'form': form})

def remove_bus(request, pk):
    bus = Bus.objects.get(id = pk)
    bus.delete()

    return redirect('bus_list')
