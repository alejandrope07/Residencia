from django.db import models
from apps.clientes.models import Clientes, Empleados, Lugar
# Create your models here.


class Reportes(models.Model):
	"""docstring for Equipo"""
	fecha_recibido = models.DateField()
	No_reporte = models.CharField(max_length=10, primary_key=True)
	cliente = models.ForeignKey(Clientes, null=True, blank=True, on_delete=models.CASCADE)
	direccion = models.TextField()
	ciudad = models.CharField(max_length=30)
	telefono = models.BigIntegerField()
	realizado = models.ForeignKey(Lugar, null=True, blank=True, on_delete=models.CASCADE)
	atendido = models.ForeignKey(Empleados, null=True, blank=True, on_delete=models.CASCADE)
	equipo_recibido = models.CharField(max_length=30)
	falla_reportada = models.CharField(max_length=40)
	trabajo_realizado = models.CharField(max_length=80)
	observaciones = models.CharField(max_length=30)
	total = models.IntegerField()
