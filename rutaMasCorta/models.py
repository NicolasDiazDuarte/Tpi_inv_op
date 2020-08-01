from django.db import models

#Clase que maneja el nodo origen cargado
class Source(models.Model):
    Nodo_Origen = models.CharField(max_length=2 , blank=False ,null=False)

    class Meta:
        verbose_name= 'Nodo_Origen'
        
    def __str__(self):
        return '{}'.format(self.source)

#Clase que maneja el nodo destino cargado
class Target(models.Model):
    Nodo_Destino = models.CharField(max_length=2 ,blank=False, null=False)
    
    class Meta:
        verbose_name= 'Nodo_Destino'

    def __str__(self):
        return '{}'.format(self.target)

#Clase que maneja el peso de la relacion entre el nodo origen y destino cargado
class Weight(models.Model):
    Peso= models.IntegerField(max_length=2, blank=False ,null=False)
    
    
    class Meta:
        verbose_name= 'Peso'

    def __str__(self):
        return '{}'.format(self.weightNro)
