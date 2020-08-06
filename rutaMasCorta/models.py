from django.db import models
from django.core.validators import validate_comma_separated_integer_list

class Rows(models.Model):
    rows= models.IntegerField(max_length=2, blank=False ,null=False)
    
    
    class Meta:
        verbose_name= 'rows'


class Nodos(models.Model):
    source= models.CharField(max_length=2, blank=False ,null=False)
    target= models.CharField(max_length=2, blank=False ,null=False)
    weight= models.IntegerField(max_length=2, blank=False ,null=False)
    
    class Meta:
        verbose_name= 'Nodos'

class Lista(models.Model):
    lista = models.CharField(validators=[validate_comma_separated_integer_list],max_length=200, blank=True, null=True,default='')

    class Meta:
        verbose_name= 'Lista'