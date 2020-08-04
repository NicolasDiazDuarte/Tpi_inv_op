from django.db import models
from django.contrib.postgres.fields import ArrayField

#Clase que maneja el nodo origen cargado
class Source(models.Model):
    Nodo_Origen = models.CharField(max_length=2 , blank=False ,null=False)

    class Meta:
        verbose_name= 'Nodo_Origen'
        

#Clase que maneja el nodo destino cargado
class Target(models.Model):
    Nodo_Destino = models.CharField(max_length=2 ,blank=False, null=False)
    
    class Meta:
        verbose_name= 'Nodo_Destino'


#Clase que maneja el peso de la relacion entre el nodo origen y destino cargado
class Weight(models.Model):
    Peso= models.IntegerField(max_length=2, blank=False ,null=False)
    
    
    class Meta:
        verbose_name= 'Peso'

    

class ArrPeso(models.Model):
    listaP = ArrayField(models.CharField(max_length=100, blank=True))
    
    class Meta:
        verbose_name= 'listaP'

    
class ArrOrigen(models.Model):
    listaO = ArrayField(models.CharField(max_length=100, blank=True))
    
    class Meta:
        verbose_name= 'listaO'



class ArrDest(models.Model):
    listaD = ArrayField(models.CharField(max_length=100, blank=True))
    
    class Meta:
        verbose_name= 'listaD'

