from django.db import models
from django.http import HttpResponse
from django.core import serializers

# Create your models here.
class Bitacora(models.Model):
    
    fecha = models.DateField()

    modelo = models.CharField(max_length=50)
    serie = models.CharField(max_length=15)
    area = models.CharField(max_length=30)
    pieza_cambiada = models.CharField(max_length=50)
    serie_piezan = models.CharField(max_length=30)
    motivo = models.CharField(max_length=70)
