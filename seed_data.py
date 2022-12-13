from ejemplo.models import Familiar, Mascota, Vehiculo

Mascota(nombre="Branca", especie="Perro").save()
Vehiculo(tipo="Auto", color="Rojo").save()

print("Se cargo con éxito los usuarios de pruebas")