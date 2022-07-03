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
    hoteles = Hotel.objects.all()
    return render(request, 'lista_hoteles.html', {'hoteles': hoteles})


def crear_hotel(request):
    formulario = Hotel_form(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('lista_hoteles')
    return render(request, 'crear-hotel.html', {'formulario': formulario})


def editar_hotel(request, id):
    hotel = Hotel.objects.get(id=id)
    formulario = Hotel_form(request.POST or None,
                            request.FILES or None, instance=hotel)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('lista_hoteles')
    return render(request, 'editar-hotel.html', {'formulario': formulario})


def eliminar_hotel(request, id):
    hotel = Hotel.objects.get(id=id)
    hotel.delete()
    return redirect('lista_hoteles')


def aboutUs(request):
    return render(request, 'aboutUs.html')
