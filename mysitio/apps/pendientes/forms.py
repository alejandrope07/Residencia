from django import forms

from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField
from apps.reportes.models import Reportes, Empleados
from apps.pendientes.models import Pendientes
from django.contrib.admin import widgets


class PendientesForm(forms.ModelForm):
	"""docstring for """
	class Meta:
		model = Pendientes

		fields = [
			'fecha',
			'descripcion',
			'asignar',

		]
		labels = {
			'fecha': 'Fecha',
			'descripcion': 'Descripcion',
			'asignar': 'Asignar a',



		}

		widgets = {
			'fecha': forms.TextInput(attrs={'class': 'form-control'}),
			'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
			'asignar': forms.Select(attrs={'class': 'form-control'}),			
		}
