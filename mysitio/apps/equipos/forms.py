from django import forms

from apps.equipos.models import Equipo



class EquiposForm(forms.ModelForm):

	class Meta:
		model = Equipo

		fields = [
		'nombre',
		'modelo',
		'No_registro',
		'fecha_recibido',

		]
		labels = {
		'nombre': 'Nombre',
		'modelo': 'Modelo',
		'No_registro': 'Numero de registro',
		'fecha_recibido': 'Fecha de recibido',


		}
		widgets = {
		'nombre': forms.TextInput(attrs={'class': 'form-control'}),
		'modelo': forms.TextInput(attrs={'class': 'form-control'}),
		'No_registro': forms.TextInput(attrs={'class': 'form-control'}),
		'fecha_recibido': forms.TextInput(attrs={'class': 'form-control'}),

		}