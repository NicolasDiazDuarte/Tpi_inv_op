from django.db import models

# Create your models here.

class InstancesNumber(models.Model):
    instancesNro= models.IntegerField(max_length=2)

    
