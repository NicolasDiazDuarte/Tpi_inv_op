from django.urls import path
from django.contrib import admin
from .views import index
from .views import redes
from rutaMasCorta.views import instanciarNodosRMC
from expansionMinima.views import instanciarNodosEM


urlpatterns = [
    path('', index, name="index"),
    path('Redes/', redes, name="redes"),
    path('RMC/', instanciarNodosRMC, name="rutaMasCorta"),
    path('EM/', instanciarNodosEM, name="expancionMinima"),
]