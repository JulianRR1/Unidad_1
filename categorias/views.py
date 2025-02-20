from django.shortcuts import render, redirect
from .models import Categoria
from django.http import JsonResponse
from .forms import categoriaForm

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

