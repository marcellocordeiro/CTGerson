from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Permission, User
from django.db.models import Min
from django.utils import timezone
from .models import Bus, Occurrence, Distance, Meshblu
from .forms import BusForm
import math


def occurrence(request):
    admin = request.user.groups.filter(name='Administrators').exists()

    #TODO: replace this with getData() / python code to extract from serial
    thing = Meshblu.objects.first()

    #update occurrence
    occurrence = Occurrence.objects.filter(closed=False, bus=thing.bus)
    occurrence.responded = True
    occurrence.response_time = timezone.localtime
    occurrence.responder = request.user
    occurrence.save()

    return render(request, 'occurrence.html', {'admin': admin, 'bus': thing.bus})


def update_occurrence(request):
    admin = request.user.groups.filter(name='Administrators').exists()

    #TODO: replace this with getData() / python code to extract from serial
    thing = Meshblu.objects.first()

    #update occurrence
    occurrence = Occurrence.objects.filter(closed=False, bus=thing.bus)
    occurrence.finish_time = timezone.localtime
    occurrence.save()

    return render(request, 'update_occurrence.html', {'admin': admin})


def update_data(request):
    if request.user.groups.filter(name='Police Officers').exists():
        #get updated information from meshblu
        #TODO: replace this with getData() / python code to extract from serial
        thing = Meshblu.objects.first()

        if thing.button:
            try:
                distance_obj = Distance.objects.get(officer=request.user)

                #get nearest officer
                min_distance = Distance.objects.all().aggregate(Min('distance'))
                nearest_officer = Distance.objects.filter(distance=min_distance["distance__min"]).first().officer

                if nearest_officer == request.user:
                    return JsonResponse({'alert': True})
                else:
                    return JsonResponse({'alert': False})
            except Distance.DoesNotExist:
                #open occurrence (firs alert signal)
                occurrence = Occurrence(bus=thing.bus, alert_time=timezone.localtime, latitude=thing.latitude, longitude=thing.longitude)
                occurrence.save()

                #get officer location
                #TODO: replace this with real location
                officer_latitude = request.user.id * 3
                officer_longitude = request.user.id * (-4)

                #calculate distance and send to web database
                distance = math.sqrt((thing.latitude - officer_latitude) ** 2 + (thing.longitude - officer_longitude) ** 2)
                distance_obj = Distance(officer=request.user, bus=thing.bus, distance=distance)
                distance_obj.save()

                return JsonResponse({'alert': False})

    return JsonResponse({'alert': False})


def update_location(request):
    if request.user.groups.filter(name='Police Officers').exists():
        #get updated information from meshblu
        #TODO: replace this with getData() / python code to extract from serial
        thing = Meshblu.objects.first()

        return JsonResponse({
            'admin': False,
            'latitude': thing.latitude,
            'longitude': thing.longitude
        })
    else:
        return JsonResponse({'admin': True})




@login_required
def home(request):
    admin = request.user.groups.filter(name='Administrators').exists()
    return render(request, 'home.html', {'admin': admin})


@login_required
@permission_required('Bus.can_see_bus_list')
def bus_list(request):
    admin = request.user.groups.filter(name='Administrators').exists()
    buses = Bus.objects.all()
    return render(request, 'bus_list.html', {'admin': admin, 'buses': buses})


@login_required
@permission_required('Bus.can_see_bus_list')
def register_bus(request):
    admin = request.user.groups.filter(name='Administrators').exists()
    if request.method == "POST":
        form = BusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bus_list')
    else:
        form = BusForm()
    return render(request, 'register_bus.html', {'admin': admin, 'form': form})


@login_required
@permission_required('Bus.can_see_bus_list')
def edit_bus(request, pk):
    admin = request.user.groups.filter(name='Administrators').exists()
    bus = get_object_or_404(Bus, pk=pk)

    if request.method == "POST":
        form = BusForm(request.POST, instance=bus)
        
        if form.is_valid():
            form.save()
            return redirect('bus_list')
    else:
        form = BusForm(instance=bus)

    return render(request, 'edit_bus.html', {'admin': admin, 'form': form})


@login_required
@permission_required('Bus.can_see_bus_list')
def remove_bus(request, pk):
    bus = Bus.objects.get(id=pk)
    bus.delete()

    return redirect('bus_list')


@login_required
@permission_required('Bus.can_see_bus_list')
def bus_detail(request, pk):
    admin = request.user.groups.filter(name='Administrators').exists()
    bus = get_object_or_404(Bus, pk=pk)
    occurrences = Occurrence.objects.filter(bus=bus)

    return render(request, 'bus_detail.html', {'admin': admin, 'bus': bus, 'occurrences': occurrences})


@login_required
def occurrences_list(request):
    admin = request.user.groups.filter(name='Administrators').exists()
    occurrences = Occurrence.objects.all().filter(closed=True)
    return render(request, 'occurrences_list.html', {'admin': admin, 'occurrences': occurrences})