from django.db import models

# Create your models here.

class Usuarios(models.Model):
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    dni=models.IntegerField()
    
    def __str__(self):
        return f'Nombre: {self.nombre}  Apellido: {self.apellido} Dni: {self.dni}'
class Actividad(models.Model):
    actividad_realizar=models.CharField(max_length=20)
    profesor=models.CharField(max_length=20)
    horarios=models.DateTimeField()
class InformacionCliente(models.Model):
    nro_afiliado=models.CharField(max_length=20)
    obra_social=models.CharField(max_length=20)
    
