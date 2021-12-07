from django.db import models

# Create your models here.

class Usuarios(models.Model):
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    dni=models.IntegerField()
    
    
class Actividad(models.Model):
    actividad_realizar=models.CharField(max_length=20)
    profesor=models.CharField(max_length=20)
    horarios=models.DateTimeField()

def __str__(self):
    return f'Nombre: {self.nombre}  Apellido: {self.apellido} DNI: {self.dni}'

class Turnos(models.Model):
    nombre = models.CharField(max_length=20)
    actividad = models.CharField(max_length=20)
    fecha_turno = models.DateTimeField()


