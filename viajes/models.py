from django.db import models

# Create your models here.

class Viaje(models.Model):
    precio = models.FloatField()
    destino = models.CharField(max_length=50)
    fecha = models.DateField()

class Destino(models.Model):
    name = models.CharField(max_length=50)
 