from django.urls import path
from viajes.views import crear_hotel, listar_viajes, listar_destinos, listar_hoteles, create_viaje, buscar_viajes, editar_hotel
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', listar_viajes, name='lista_viajes'),
    path('destinos/', listar_destinos, name='lista_destinos'),
    path('hoteles/', listar_hoteles, name='lista_hoteles'),
    path('buscar-viajes/', buscar_viajes, name='buscar-viajes'),
    path('crear-viajes/', login_required(create_viaje), name='create_viaje'),
    path('crear-hotel/', login_required(crear_hotel), name='crear_hotel'),
    path('editar-hotel/', login_required(editar_hotel), name='editar_hotel'),


]
