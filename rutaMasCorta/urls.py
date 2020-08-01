from django.urls import path 
from .views import instanciarNodos

urlpatterns = [
    path('RMC/',instanciarNodos)
]