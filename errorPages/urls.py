"""
URL configuration for errorPages project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path, include

from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('error/', error, name='error'),
    path('onepage/', onepage, name='onepage'),
    path('prueba/', prueba, name='prueba'),
    path('buscar/', search_view, name='search_view'),
    
    path('error_logs/', users_logs, name='error_logs'),
    path('api/error_logs/', get_users_logs, name='get_error_logs'),
    path('users/', include('users.urls')),
    path('productos/', include('productos.urls')),
    path('categoria/', include('categorias.urls')),
    path('alumnos/', include('alumnos.urls')),
]
