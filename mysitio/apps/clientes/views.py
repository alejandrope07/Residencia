from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, ListView, DeleteView

from django.urls import reverse_lazy
from django.http import HttpResponse


from apps.clientes.forms import ClientesForms, EmpleadosForms, LugarForms

from apps.clientes.models import Clientes, Empleados, Lugar
# Create your views here.
class ClientesCrear(CreateView):
	"""vistas basadas en clases"""
	model = Clientes
	form_class = ClientesForms
	template_name = 'sistema/cliente_form.html'
	success_url = reverse_lazy('reportes_listar')

class EmpleadosCrear(CreateView):
	"""docstring for EmpleadosCrear"""
	model = Empleados
	form_class = EmpleadosForms
	template_name = 'sistema/empleados_form.html'
	success_url = reverse_lazy('reportes_listar')
