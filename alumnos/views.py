from .models import Alumno
from .forms import alumnoForm 
from .serializers import AlumnoSerializer
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from django.shortcuts import render

class AlumnoViewset(viewsets.ModelViewSet):
    #1. Saber a que objeto hace referencia
    queryset = Alumno.objects.all()
    
    #2. Serializar los objetos
    serializer_class = AlumnoSerializer

    #3. Renderizar respuestas
    render_classes = [JSONRenderer]

    #4. Metodos
    #http_method_names = ['GET', 'POST']
# Create your views here.

def formView(request):
    form = alumnoForm()
    return render(request, 'jose_julian.html', {'form': form})
