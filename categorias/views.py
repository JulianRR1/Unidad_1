from django.shortcuts import render, redirect
from .models import Categoria
from django.http import JsonResponse
from .forms import categoriaForm
import json

def lista_categorias(request):
    categorias = Categoria.objects.all()

    data=[
        {
            'nombre': c.nombre,
            'imagen': c.imagen
        }
        for c in categorias
    ]

    return JsonResponse(data, safe=False)

def agregar_categoria(request):
    if request.method == 'POST':
        form=categoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categorias')
    else:
        form = categoriaForm()
    return render(request, 'regCategoria.html', {'form': form})
# Create your views here.

def vista_categorias(request):
    return render(request, 'categorias.html')



def registrar_categoria(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body) #Hace que el parametro se vuelva json
            categoria = Categoria.objects.create(
                nombre = data['nombre'],
                imagen = data['imagen']
            )
            return JsonResponse({'mensaje': 'Registro exitoso', 'id':categoria.id},status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Metodo no soportado'}, status=405)