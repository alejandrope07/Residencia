from django import forms

from apps.reportes.models import Reportes

class ReportesForms(forms.ModelForm):

	class Meta:
		model = Reportes

		fields = [
			'fecha_recibido',
			'No_reporte',
			'cliente',
			'direccion',
			'ciudad',
			'telefono',
			'atendido',
			'equipo_recibido',
			'falla_reportada',
			'trabajo_realizado',
			'observaciones',

		]
		labels = {
			'fecha_recibido': 'Fecha de recibido',
			'No_reporte': 'Numero de reporte',
			'cliente': 'Cliente',
			'direccion': 'Direccion',
			'ciudad': 'Ciudad',
			'telefono': 'Telefono',
			'atendido': 'Atendido por',
			'equipo_recibido': 'Equipo recibido',
			'falla_reportada': 'Falla Reportada',
			'trabajo_realizado': 'trabajo realizado',
			'observaciones': 'Observaciones del equipo',

		}
		
		widgets = {
			'fecha_recibido': forms.TextInput(attrs={'class': 'form-control'}),
			'No_reporte': forms.TextInput(attrs={'class': 'form-control'}),
			'cliente': forms.TextInput(attrs={'class': 'form-control'}),
			'direccion': forms.TextInput(attrs={'class': 'form-control'}),
			'ciudad': forms.TextInput(attrs={'class': 'form-control'}),
			'telefono': forms.TextInput(attrs={'class': 'form-control'}),
			'atendido': forms.Select(attrs={'class': 'form-control'}),
			'equipo_recibido': forms.TextInput(attrs={'class': 'form-control'}),
			'falla_reportada': forms.TextInput(attrs={'class': 'form-control'}),
			'trabajo_realizado': forms.TextInput(attrs={'class': 'form-control'}),
			'observaciones': forms.TextInput(attrs={'class': 'form-control'}),
		}