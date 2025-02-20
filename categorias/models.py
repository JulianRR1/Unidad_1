from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.URLField()

    def _str_(self):
        return self.nombre

# Create your models here.
