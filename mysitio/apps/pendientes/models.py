from django.db import models
from django.http import HttpResponse

from apps.clientes.models import Clientes, Empleados, Lugar
# Create your models here.
class Pendientes(models.Model):
    
    fecha = models.DateField()

    descripcion = models.CharField(max_length=50)
    asignar = models.ForeignKey(Empleados, null=True, blank=True, on_delete=models.CASCADE)
    
