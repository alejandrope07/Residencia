from django.db import models

# Create your models here.


class Empleados(models.Model):
		nombre = models.CharField(max_length=30)

		def __str__(self):
			return '{}'.format(self.nombre)

class Reportes(models.Model):
	"""docstring for Equipo"""
	fecha_recibido = models.DateField()
	No_reporte = models.CharField(max_length=10, primary_key=True)
	cliente = models.CharField(max_length=50)
	direccion = models.TextField()
	ciudad = models.CharField(max_length=30)
	telefono = models.IntegerField()
	
	atendido = models.ManyToManyField(Empleados, blank=True)
	equipo_recibido = models.CharField(max_length=30)
	falla_reportada = models.CharField(max_length=40)
	trabajo_realizado = models.CharField(max_length=80)
	observaciones = models.CharField(max_length=30)