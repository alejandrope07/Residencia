from django import forms

from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField
from apps.reportes.models import Reportes, Empleados
from apps.bitacora.models import Bitacora
from django.contrib.admin import widgets


class BitacoraForm(forms.ModelForm):
	"""docstring for """
	class Meta:
		model = Bitacora

		fields = [
			'fecha',
			'modelo',
			'serie',
			'area',
			'pieza_cambiada',
			'serie_piezan',
			'motivo',


		]
		labels = {
			'fecha': 'Fecha',
			'modelo': 'Modelo',
			'serie': 'Serie',
			'area': 'Area',
			'pieza_cambiada': 'Pieza Cambiada',
			'serie_piezan': 'Serie pieza nueva',
			'motivo': 'Motivo',



		}

		widgets = {
			'fecha': forms.TextInput(attrs={'class': 'form-control'}),
			'modelo': forms.TextInput(attrs={'class': 'form-control'}),
			'serie': forms.TextInput(attrs={'class': 'form-control'}),			
			'area': forms.TextInput(attrs={'class': 'form-control'}),
			'pieza_cambiada': forms.TextInput(attrs={'class': 'form-control'}),
			'serie_piezan': forms.TextInput(attrs={'class': 'form-control'}),
			'motivo': forms.TextInput(attrs={'class': 'form-control'}),

		}



