from django import forms

class Viaje_form(forms.Form):
    precio = forms.FloatField()
    destino = forms.CharField()
    fecha_salida = forms.DateField()
    fecha_regreso = forms.DateField()


