from django import forms
from viajes.models import Hotel


class Viaje_form(forms.Form):
    precio = forms.FloatField()
    destino = forms.CharField()
    fecha_salida = forms.DateField()
    fecha_regreso = forms.DateField()


class Hotel_form(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = '__all__'
