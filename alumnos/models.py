from django.db import models

class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.PositiveIntegerField()
    matricula = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)


    def _str_(self):
        return self.nombre
# Create your models here.
