from django.db import models

class Familiar(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    numero_pasaporte = models.IntegerField()
    
    def __str__(self):
      return f"{self.nombre}, {self.numero_pasaporte}, {self.direccion}, {self.id}"

class Mascota(models.Model):
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=200)
    
    
    def __str__(self):
      return f"{self.nombre}, {self.especie}, {self.id}"

class Vehiculo(models.Model):
    tipo = models.CharField(max_length=100)
    color = models.CharField(max_length=200)
    
    
    def __str__(self):
      return f"{self.tipo}, {self.color}, {self.id}"
