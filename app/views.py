from django.http import HttpResponse
from django.shortcuts import render
import requests
from django.conf import settings

from django.http import JsonResponse
from django.shortcuts import render
from .models import Usuarios

#from .utils import 
GOOGLE_API_KEY = getattr(settings, "GOOGLE_API_KEY", "")
SEARCH_ENGINE_ID = getattr(settings, "SEARCH_ENGINE_ID", "")

def index(request):
    return HttpResponse("<h1>Hola Mundo</h1>")

def error_404_view(request, exception):
    render(request, '404.html', status=404)

def error_500_view(request, exception):
    render(request, '500.html', status=500)

def error(request, exception):
    return 7/0

def onepage(request):
    return render(request, 'onepage.html', status=200)

def prueba(request):
    #Como obtener informacion de un HTML
    nombre = request.GET.get('nombre', '')
    edad = request.GET.get('edad', '')
    persona = {
        'nombres': nombre,
        'edad': edad,
        'descripcion': nombre + " - " + edad
    }

    persona2 = {
        'nombres': 'nancy',
        'edad': '30',
        'descripcion': nombre + " - " + edad
    }

    persona3 = {
        'nombres': 'david',
        'edad': '25',
        'descripcion': nombre + " - " + edad
    }

    if(persona['nombres'] == 'julian'):
        persona['descripcion'] = 'Bienvenido Usuario administrador'
    
    print(persona['nombres'])

    conjunto = [persona, persona2, persona3]

    return render(
        request,
        'prueba.html',
        {'objeto': persona, 'saludo': 'Hola mundo', 'personas': conjunto}
    )

def google_search(query):
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "q": query,
        "key": GOOGLE_API_KEY,
        "cx": SEARCH_ENGINE_ID
    }
    response = requests.get(url, params=params)
    return response.json()

def search_view(request):
    query = request.GET.get("q", "")
    results = []
    if query:
        data = google_search(query)
        results = data.get("items", [])

    return render(request, "search.html", {"results": results, "query": query})

def get_users_logs(request):
    users = Usuarios.objects.values('nombre', 'apellidos', 'matricula', 'edad')
    return JsonResponse({'data': list(users)})

def users_logs(request):
    return render(request, 'usuarios.html')

