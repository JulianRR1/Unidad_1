from django.urls import path, include
from .views import *
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
#Registrar path comun para las rutas
router.register(r'api',AlumnoViewset)

urlpatterns = [
    path('formulario/', formView, name='formulario'),
    path('', include(router.urls)),
]