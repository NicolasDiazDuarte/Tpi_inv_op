from django.db import models

#Clase que maneja el nodo origen cargado
class Source(models.Model):
    source = models.CharField(max_length=2 , blank=False ,null=False)

    class Meta:
        verbose_name= 'Source'
        
    def __str__(self):
        return '{}'.format(self.source)

#Clase que maneja el nodo destino cargado
class Target(models.Model):
    target = models.CharField(max_length=2 ,blank=False, null=False)
    
    class Meta:
        verbose_name= 'Target'

    def __str__(self):
        return '{}'.format(self.target)

#Clase que maneja el peso de la relacion entre el nodo origen y destino cargado
class Weight(models.Model):
    weightNro = models.IntegerField(max_length=2, blank=False ,null=False)
    
    class Meta:
        verbose_name= 'Weight'

    def __str__(self):
        return '{}'.format(self.weightNro)
