from django.db import models

# Create your models here.
from django.db import models

class EmpleadoModel(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    sueldo = models.IntegerField() 

