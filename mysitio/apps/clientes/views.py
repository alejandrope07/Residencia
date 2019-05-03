from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, ListView, DeleteView

from django.urls import reverse_lazy
from django.http import HttpResponse
from django.core import serializers
import json
from apps.clientes.forms import ClientesForms, EmpleadosForms, LugarForms
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.clientes.models import Clientes, Empleados, Lugar
# Create your views here.
class ClientesCrear(CreateView):
	"""vistas basadas en clases"""
	model = Clientes
	form_class = ClientesForms
	template_name = 'sistema/cliente_form.html'
	success_url = reverse_lazy('clientes_lista')

class EmpleadosCrear(CreateView):
	"""docstring for EmpleadosCrear"""
	model = Empleados
	form_class = EmpleadosForms
	template_name = 'sistema/empleados_form.html'
	success_url = reverse_lazy('reportes_listar')

class ClienteEditar(UpdateView):
	model = Clientes
	form_class = ClientesForms
	template_name = 'sistema/clientes_edit.html'
	success_url = reverse_lazy('clientes_lista')

class ClienteView(UpdateView):
	model = Clientes
	form_class = ClientesForms
	template_name = 'sistema/clientes_view.html'
	success_url = reverse_lazy('clientes_lista')

class ClienteDelete(DeleteView):
	"""docstring for ReportesDelete"""
	model = Clientes
	template_name = 'sistema/clientes_delete.html'
	success_url = reverse_lazy('clientes_lista')

class EmpleadosList(LoginRequiredMixin, ListView):
	"""docstring for ReportesList"""
	login_url = 'login'
	redirect_field_name = 'redirect_to'
	model = Empleados
	template_name = 'sistema/empleados_lista.html'
	paginate_by = 3

class ClientesList(LoginRequiredMixin, ListView):
	"""docstring for ReportesList"""
	login_url = 'login'
	redirect_field_name = 'redirect_to'
	model = Clientes
	template_name = 'sistema/clientes_lista.html'
	paginate_by = 3
	
def CargarClientes(request):
		
		if request.is_ajax:			
			clave = request.GET.get('cliente')
			data = serializers.serialize('json',Clientes.objects.all().filter(id=clave))
			
		else:
			data = 'fallo'

		return HttpResponse(data, content_type='application/json')
		