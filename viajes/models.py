from distutils.command.upload import upload
from django.db import models
from django.utils.timezone import now
from requests import delete

# Create your models here.


class Viaje(models.Model):
    precio = models.FloatField()
    destino = models.CharField(max_length=50)
    fecha_salida = models.DateField(default=now)
    fecha_regreso = models.DateField(null=True, blank=True)

    def __str__(self):
        fila = "Destino: " + self.destino + " - " + " Salida: " + str(self.fecha_salida) + \
            " Regreso: " + str(self.fecha_regreso) + \
            " - " + " Precio: $" + str(self.precio)
        return fila


class Destino(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(blank=True, null=True, upload_to='destinos')

    def __str__(self):
        return self.name


class Hotel(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, verbose_name='Titulo')
    pais = models.CharField(max_length=20)
    descripcion = models.TextField(null=True, verbose_name='Descripcion')
    imagen = models.ImageField(
        blank=True, null=True, upload_to='media/', verbose_name='Imagen')
    precio = models.FloatField()

    def __str__(self):
        fila = "Nombre: " + self.nombre + " - " + " Pais: " + \
            self.pais + " - " + " Precio: $" + str(self.precio)
        return fila
