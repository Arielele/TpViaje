from django.shortcuts import render



# Create your views here.

def bienvenida(request):
   
    return render ( request, 'bienvenida.html',)
