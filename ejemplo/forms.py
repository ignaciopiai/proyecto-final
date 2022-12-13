from django import forms
from ejemplo.models import Familiar, Mascota, Vehiculo

class Buscar(forms.Form):
    nombre = forms.CharField(max_length=100)

class FamiliarForm(forms.ModelForm):
  class Meta:
    model = Familiar
    fields = ['nombre', 'direccion', 'numero_pasaporte']

class MascotaForm(forms.ModelForm):
  class Meta:
    model = Mascota
    fields = ['nombre', 'especie']

class VehiculoForm(forms.ModelForm):
  class Meta:
    model = Vehiculo
    fields = ['tipo', 'color']