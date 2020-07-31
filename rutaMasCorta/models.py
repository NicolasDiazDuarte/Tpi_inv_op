from django.db import models

#Numero de veces que se va a instanciar un nodo con otro agregandole un peso
class InstancesNumber(models.Model):
    instancesNro= models.IntegerField(max_length=2)

class Source(models.Model):
    source=models.CharField(max_length=2)

class Target(models.Model):
    target=models.CharField(max_length=2)

class Weight(models.Model):
    weightNro= models.IntegerField(max_length=2)