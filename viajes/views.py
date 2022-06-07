from multiprocessing import context
from django.shortcuts import render

from viajes.models import Viaje, Destino, Hotel
from viajes.forms import Viaje_form

# Create your views here.

def listar_viajes(request):
    lista_viajes = Viaje.objects.all()
    context = {'lista_viajes': lista_viajes}

    return render ( request, 'lista_viajes.html', context=context)


def listar_destinos(request):
    lista_destinos = Destino.objects.all()
    context = {'lista_destinos': lista_destinos}

    return render ( request, 'lista_destinos.html', context=context)

def listar_hoteles(request):
    lista_hoteles = Hotel.objects.all()
    context = {'lista_hoteles': lista_hoteles}
    
    return render ( request, 'lista_hoteles.html', context=context)

def create_viaje(request):
    form= Viaje_form()
    context = {'form': form}
    return render( request, 'create_viaje.html', context = context )
