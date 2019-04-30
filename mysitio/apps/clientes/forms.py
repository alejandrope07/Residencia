from django import forms
from apps.clientes.models import Clientes, Empleados, Lugar


class ClientesForms(forms.ModelForm):

	class Meta:
		model = Clientes
		fields = [
			'cliente',
			'direccion',
			'ciudad',
			'telefono',
			'email',


		]
		labels = {
			'cliente': 'Cliente',
			'direccion': 'Dirección',
			'ciudad': 'Ciudad',
			'telefono': 'Telefono',
			'email': 'E-mail',


		}
		
		widgets = {
			'cliente': forms.TextInput(attrs={'class': 'form-control'}),
			'direccion': forms.TextInput(attrs={'class': 'form-control'}),
			'ciudad': forms.TextInput(attrs={'class': 'form-control'}),
			'telefono': forms.TextInput(attrs={'class': 'form-control'}),
			'email': forms.TextInput(attrs={'class': 'form-control'}),
		}

class EmpleadosForms(forms.ModelForm):

	class Meta:
		model = Empleados
		fields = [
			'nombre',
			'apellidos',
			'domicilio',
			'telefono',
			'email',
		]
			
		labels = {
			'nombre': 'Nombre',
			'apellidos': 'Apellidos',
			'domicilio': 'Domicilio',
			'telefono': 'Telefono',
			'email': 'E-mail',
		}

		widgets = {
			'nombre': forms.TextInput(attrs={'class': 'form-control'}),
			'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
			'domicilio': forms.TextInput(attrs={'class': 'form-control'}),
			'telefono': forms.TextInput(attrs={'class': 'form-control'}),
			'email': forms.TextInput(attrs={'class': 'form-control'}),
		}

class LugarForms(forms.ModelForm):

	class Meta:
		model = Lugar
		fields = [
			'nombre',

		]

		labels = {
			'nombre': 'Nombre',
		}

		widgets = {

			'nombre': forms.TextInput(attrs={'class': 'form-control'}),
		}

