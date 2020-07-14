from django.contrib import admin
from django.urls import path
from Comedores.copa_de_leche.views import listado
from Comedores.copa_de_leche.views import buscar, ingresoEscuelas
from Comedores.copa_de_leche.views import modificar_f1, modificar, eliminar_f1, eliminar
from Comedores.copa_de_leche.views import responsable, contacto
urlpatterns = [
    path('comedores', listado),
    path('buscar', buscar),
    path('ingresar', ingresoEscuelas),
    path('modificar_f1', modificar_f1),
    path('modificar', modificar),
    path('eliminar_f1', eliminar_f1),
    path('eliminar', eliminar),
    path('responsable', responsable),
    path('contacto', contacto),
]
