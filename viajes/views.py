from http.client import HTTPResponse
from multiprocessing import context
from django.shortcuts import redirect, render
from django.http import HttpResponse

from viajes.models import Viaje, Destino, Hotel
from viajes.forms import Viaje_form, Hotel_form


from django.contrib.auth.decorators import login_required
# Create your views here.


def listar_viajes(request):
    lista_viajes = Viaje.objects.all()
    context = {'lista_viajes': lista_viajes}

    return render(request, 'lista_viajes.html', context=context)


def listar_destinos(request):
    lista_destinos = Destino.objects.all()
    context = {'lista_destinos': lista_destinos}

    return render(request, 'lista_destinos.html', context=context)


def listar_hoteles(request):
    lista_hoteles = Hotel.objects.all()
    context = {'lista_hoteles': lista_hoteles}

    return render(request, 'lista_hoteles.html', context=context)


def create_viaje(request):
    if request.method == 'GET':
        form = Viaje_form()
        context = {'form': form}
        return render(request, 'crear-viajes.html', context=context)
    else:
        form = Viaje_form(request.POST)
        if form.is_valid():
            new_viaje = Viaje.objects.create(
                precio=form.cleaned_data['precio'],
                destino=form.cleaned_data['destino'],
                fecha_salida=form.cleaned_data['fecha_salida'],
                fecha_regreso=form.cleaned_data['fecha_regreso'],
            )
            context = {'new_viaje': new_viaje}
        return render(request, 'crear-viajes.html', context=context)


def buscar_viajes(request):
    print(request.GET)
    viajes = Viaje.objects.filter(destino__icontains=request.GET['buscar'])
    context = {'viajes': viajes}
    return render(request, 'buscar-viajes.html', context=context)


def listar_hoteles(request):
    return render(request, 'lista_hoteles.html')
