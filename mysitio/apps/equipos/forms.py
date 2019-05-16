from django import forms

from apps.equipos.models import Equipo



class EquiposForm(forms.ModelForm):

	class Meta:
		model = Equipo

		fields = [
		'nombre',
		'descripcion',
		'fecha_recibido',
		'area',
		'costo',

		]
		labels = {
		'nombre': 'Nombre',
		'descripcion': 'Descripción',
		'fecha_recibido': 'Fecha recibido',
		'costo': 'Costo',
		'area': 'Área',



		}
		widgets = {
		'nombre': forms.TextInput(attrs={'class': 'form-control'}),
		'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
		'costo': forms.TextInput(attrs={'class': 'form-control'}),
		'fecha_recibido': forms.TextInput(attrs={'class': 'form-control'}),
		'area': forms.Select(attrs={'class': 'form-control'}),
		}


	