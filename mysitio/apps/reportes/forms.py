from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField
from apps.reportes.models import Reportes, Empleados
from django.contrib.admin import widgets 

class ReportesForms(forms.ModelForm):

	class Meta:
		model = Reportes
		fields = [
			'fecha_recibido',
			'id',
			'cliente',
			'direccion',
			'ciudad',
			'telefono',
			'email',
			'realizado',
			'atendido',
			'equipo_recibido',
			'falla_reportada',
			'trabajo_realizado',
			'observaciones',
			'total',

		]
		labels = {
			'fecha_recibido': 'Fecha de recibido',
			'id': 'Numero de reporte',
			'cliente': 'Cliente',
			'direccion': 'Direccion',
			'ciudad': 'Ciudad',
			'telefono': 'Telefono',
			'email': 'E-mail',
			'realizado': 'Servicio aplicado en',
			'atendido': 'Atendido por',
			'equipo_recibido': 'Equipo recibido',
			'falla_reportada': 'Falla Reportada',
			'trabajo_realizado': 'trabajo realizado',
			'observaciones': 'Observaciones del equipo',
			'total': 'Total',

		}
		
		widgets = {
			'fecha_recibido': forms.TextInput(attrs={'class': 'form-control'}),
			'id': forms.TextInput(attrs={'class': 'form-control'}),
			'cliente': forms.Select(attrs={'class': 'form-control'}),
			'direccion': forms.TextInput(attrs={'class': 'form-control'}),
			'ciudad': forms.TextInput(attrs={'class': 'form-control'}),
			'telefono': forms.TextInput(attrs={'class': 'form-control'}),
			'email': forms.TextInput(attrs={'class': 'form-control'}),
			'realizado': forms.Select(),
			'atendido': forms.Select(attrs={'class': 'form-control'}),
			'equipo_recibido': forms.TextInput(attrs={'class': 'form-control'}),
			'falla_reportada': forms.TextInput(attrs={'class': 'form-control'}),
			'trabajo_realizado': forms.TextInput(attrs={'class': 'form-control'}),
			'observaciones': forms.TextInput(attrs={'class': 'form-control'}),
			'total': forms.TextInput(attrs={'class': 'form-control'}),
		}