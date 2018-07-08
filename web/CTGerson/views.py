from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Permission
from .models import Bus, Occurrence
from .forms import BusForm


def update_data(request):
    data = {
        'button_status': Occurrence.objects.all()[0].responded    #getData()
    }
    return JsonResponse(data)


@login_required
def home(request):
    permission = Permission.objects.filter(user=request.user, codename='can_see_bus_list')
    return render(request, 'home.html', {'permission': permission})


@login_required
@permission_required('Bus.can_see_bus_list')
def bus_list(request):
    buses = Bus.objects.all()
    return render(request, 'bus_list.html', {'buses': buses})


@login_required
@permission_required('Bus.can_see_bus_list')
def register_bus(request):
    if request.method == "POST":
        form = BusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bus_list')
    else:
        form = BusForm()
    return render(request, 'register_bus.html', {'form': form})


@login_required
@permission_required('Bus.can_see_bus_list')
def edit_bus(request, pk):
    bus = get_object_or_404(Bus, pk=pk)

    if request.method == "POST":
        form = BusForm(request.POST, instance=bus)
        
        if form.is_valid():
            form.save()
            return redirect('bus_list')
    else:
        form = BusForm(instance=bus)

    return render(request, 'edit_bus.html', {'form': form})


@login_required
@permission_required('Bus.can_see_bus_list')
def remove_bus(request, pk):
    bus = Bus.objects.get(id=pk)
    bus.delete()

    return redirect('bus_list')


@login_required
@permission_required('Bus.can_see_bus_list')
def bus_detail(request, pk):
    bus = get_object_or_404(Bus, pk=pk)
    occurrences = Occurrence.objects.filter(bus=bus)

    return render(request, 'bus_detail.html', {'bus': bus, 'occurrences': occurrences})


@login_required
def occurrences_list(request):
    occurrences = Occurrence.objects.all()
    return render(request, 'occurrences_list.html', {'occurrences': occurrences})