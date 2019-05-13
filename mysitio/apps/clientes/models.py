from django.db import models
from django.http import HttpResponse
from django.core import serializers

# Create your models here.
class Clientes(models.Model):
	"""docstring for Equipo"""
	cliente = models.CharField(max_length=50)
	direccion = models.TextField()
	ciudad = models.CharField(max_length=30)
	telefono = models.BigIntegerField()
	email = models.CharField(max_length=30)


	def __str__(self):
			return '{}'.format(self.cliente)



class Empleados(models.Model):
	nombre = models.CharField(max_length=50)
	apellidos = models.CharField(max_length=60)
	domicilio = models.CharField(max_length=70)
	telefono = models.BigIntegerField()
	email = models.CharField(max_length=30)

	def __str__(self):
			return '{}'.format(self.nombre)

class Lugar(models.Model):
	nombre = models.CharField(max_length=30)
	def __str__(self):
			return '{}'.format(self.nombre)

class Area(models.Model):
	nombre = models.CharField(max_length=30)