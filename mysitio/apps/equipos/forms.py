from django import forms

from apps.equipos.models import Equipo



class EquiposForm(forms.ModelForm):

	class Meta:
		model = Equipo

		fields = [
		'cantidad',
		'nombre',
		'descripcion',
		'proveedor',
		'fecha_recibido',
		'cliente',
		'precio',

		]
		labels = {
		'cantidad': 'Cantidad',
		'nombre': 'Nombre',
		'descripcion': 'Descripción',
		'proveedor': 'Proveedor',
		'fecha_recibido': 'Fecha recibido',
		'cliente': 'Cliente',
		'precio': 'precio',



		}
		widgets = {
		'cantidad': forms.TextInput(attrs={'class': 'form-control'}),
		'nombre': forms.TextInput(attrs={'class': 'form-control'}),
		'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
		'proveedor': forms.TextInput(attrs={'class': 'form-control'}),
		'fecha_recibido': forms.TextInput(attrs={'class': 'form-control'}),
		'cliente': forms.Select(attrs={'class': 'form-control'}),
		'precio': forms.TextInput(attrs={'class': 'form-control'}),
		}


	