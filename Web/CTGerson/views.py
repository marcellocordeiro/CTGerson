from django.shortcuts import render
from django.http import HttpResponse
from .models import Bus

def initial(request):
    buses = Bus.objects.all()

    return render(request, 'initial.html', {'buses': buses})