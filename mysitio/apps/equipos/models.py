from django.db import models

# Create your models here.

class Equipo(models.Model):
	"""docstring for Equipo"""
	nombre = models.CharField(max_length=40)
	modelo = models.CharField(max_length=30)
	No_registro = models.CharField(max_length=10, primary_key=True)
	fecha_recibido = models.DateField()