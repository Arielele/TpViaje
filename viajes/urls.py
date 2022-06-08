from django.urls import path

from viajes.views import listar_viajes, listar_destinos, listar_hoteles, create_viaje, buscar_viajes

urlpatterns = [
    path('', listar_viajes, name = 'lista_viajes'),
    path('destinos/', listar_destinos, name = 'lista_destinos'),
    path('hoteles/', listar_hoteles, name='lista_hoteles'),
    path('create_viaje/', create_viaje, name='create_viaje'),
    path('buscar-viajes/', buscar_viajes, name ='buscar-viajes')
]