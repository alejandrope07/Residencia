from django.db import models
from apps.clientes.models import Clientes, Empleados, Lugar, Area
# Create your models here.


class Equipo(models.Model):
	"""docstring for Equipo"""
	nombre = models.CharField(max_length=40)
	descripcion = models.CharField(max_length=50)
	fecha_recibido = models.DateField()
	area = models.ForeignKey(Area, null=True, blank=True, on_delete=models.CASCADE)
	costo = models.IntegerField()
