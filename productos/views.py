from .models import Producto
from .serializers import ProductoSerializer
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer

class ProductoViewset(viewsets.ModelViewSet):
    #1. Saber a que objeto hace referencia
    queryset = Producto.objects.all()
    
    #2. Serializar los objetos
    serializer_class = ProductoSerializer

    #3. Renderizar respuestas
    render_classes = [JSONRenderer]

    #4. Metodos
    #http_method_names = ['GET', 'POST']

from .forms import productoForm
from django.shortcuts import render
def agregar_producto(request):
    form = productoForm()
    return render(request, 'agregar.html', {'form':form})