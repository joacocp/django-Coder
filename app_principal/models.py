from django.db import models


class Familiar(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    fecha_de_nacimiento = models.DateField()
    
    def __str__(self):
        return f'{self.nombre} {self.apellido} de {self.edad} años de edad. Nacio el {self.fecha_de_nacimiento}.'
    
    
# Create your models here.
