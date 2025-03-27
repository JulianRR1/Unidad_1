from django.db import models

class Detalles_Producto(models.Model):
    descripcion = models.TextField(max_length=400)
    fecha_caducidad = models.DateField()

class Proveedor(models.Model):
    nombre =models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)
#Cambios para relaciones
#oneToOneField ==> 1:1
#Foreing ==> 1:M
#ManyToManyField => M:M

from categorias.models import Categoria

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.URLField()
    #RELACIONES
    #1:1
    detalles_producto = models.OneToOneField(Detalles_Producto, null=True, blank=True, on_delete = models.CASCADE)

    #1:M
    categoria = models.ForeignKey(Categoria, null=True, blank=True, on_delete = models.CASCADE)

    #M:M
    proveedor = models.ManyToManyField(
        #through = Modelo_personalizado
        Proveedor, 
        null=True, 
        blank=True
    )

    def _str_(self):
        return self.nombre
# Create your models here.


#python manage.py makemigrations alumnos productos
#python manage.py migrate