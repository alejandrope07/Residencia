from django.db import models

# Create your models here.


class Equipo(models.Model):
	"""docstring for Equipo"""
	cantidad = models.IntegerField()
	nombre = models.CharField(max_length=40)
	descripcion = models.CharField(max_length=50)
	proveedor = models.CharField(max_length=30)
	fecha_recibido = models.DateField()
	cliente = models.CharField(max_length=40)
	precio = models.IntegerField()
