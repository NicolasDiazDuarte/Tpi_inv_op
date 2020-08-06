from django.db import models

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

#Clase que maneja el peso de la relacion entre el nodo origen y destino cargado
class Rows(models.Model):
    rows= models.IntegerField(max_length=2, blank=False ,null=False)
    
    
    class Meta:
        verbose_name= 'rows'

