from django import forms

class Viaje_form(forms.Form):
    precio = forms.FloatField()
    destino = forms.CharField()
    fecha_salida = forms.DateField()
    fecha_regreso = forms.DateField()


# class Hotel_form(forms.Form):
#     nombre = forms.CharField(max_length=30)
#     provincia = forms.CharField(max_length=20)
#     domicilio = forms.CharField(max_length=50)
#     precio = forms.FloatField()