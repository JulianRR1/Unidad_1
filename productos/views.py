from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Producto
from .forms import productoForm
import json

#Metodo que devuelve el JSON
def lista_productos(request):
    productos = Producto.objects.all()

    data=[
        {
            'id': p.id,
            'nombre': p.nombre,
            'precio': p.precio,
            'imagen': p.imagen
        }
        for p in productos
    ]

    return JsonResponse(data, safe=False)


def agregar_producto(request):
    if request.method == 'POST':
        form=productoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista')
    else:
        form = productoForm()
    return render(request, 'agregar.html', {'form': form})
# Create your views here.

#Funcion que registre sin recargar la pagina
def registrar_producto(request):
    #Checar si se maneja POST
    if request.method == 'POST':
        try:
            #Intentar optener los datos del body
            data = json.loads(request.body) #Hace que el parametro se vuelva json
            producto = Producto.objects.create(
                #Es un constructor
                nombre = data['nombre'],
                precio = data['precio'],
                imagen = data['imagen']
            )
            return JsonResponse({'mensaje': 'Registro exitoso', 'id':producto.id},status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Metodo no soportado'}, status=405)


#API PUT
def actualizar_producto(request, id_producto):
    if request.method == 'PUT':
        #Obtener entidad especifico
        #Parametros: modelo y id
        producto = get_object_or_404(Producto, id=id_producto)
        try:
            #Actualizar con informacion recibida en el cuerpo
            data = json.loads(request.body)

            #Actualizar cada campo disponible
            producto.nombre = data.get('nombre', producto.nombre)
            producto.precio = data.get('precio', producto.precio)
            producto.imagen = data.get('imagen', producto.imagen)
            producto.save()

            #Retornar respuesta de success
            return JsonResponse({'mensaje': 'Producto actualizado correctamente'}, status=200)
        except Exception as e:
            return JsonResponse({'Error': str(e)}, status=400)
    return JsonResponse({'ERROR': 'Metodo no soportado'}, status=405)


#API DELETE
def borrar_producto(request, id_producto):
    if request.method == 'DELETE':
        producto = get_object_or_404(Producto, id=id_producto)
        producto.delete() #Borra de la base de datos directamente
        return JsonResponse({'mensaje': 'Producto borrado exitosamente'}, status=200)
    return JsonResponse({'ERROR': 'Metodo no soportado'}, status=405)

#Metodo que devuelve uno en especifico

def obtner_producto(request, id_producto):
    if request.method == 'GET':
        producto = get_object_or_404(Producto, id=id_producto)
        data = {
            'id': producto.id,
            'nombre': producto.nombre,
            'precio': producto.precio,
            'imagen': producto.imagen
        }
        return JsonResponse(data, status=200)
    return JsonResponse({'ERROR': 'Metodo no soportado'}, status=405)