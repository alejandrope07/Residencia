from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.core import serializers

from apps.reportes.forms import ReportesForms
from apps.clientes.models import Clientes
from apps.reportes.models import Reportes, Empleados

# Create your views here.
def index(request):
	return render(request, 'sistema/index.html')

def inicio(request):
	return render(request, 'sistema/inicio_form.html')


def validar_usuario(request):
	if not request.user.is_authenticated:
		return redirect('login')

def reportes_view(request):
	if request.method == 'POST':
		form = ReportesForms(request.POST)
		if form.is_valid():
			form.save()

		return redirect('reportes_listar')

	else:
		form = ReportesForms()

	return render(request, 'sistema/reportes_form.html', {'form': form})
"""
def reportes_lista(request):
	reportes = Reportes.objects.all().order_by('No_reporte')
	contexto = {'reportes':reportes}
	return render(request, 'sistema/reportes_lista.html', contexto)


def reportes_editar(request, No_reporte):
	reportes = Reportes.objects.get(No_reporte = No_reporte)
	if request.method == 'GET':
		form = ReportesForms(instance=reportes)
	else:
		form = ReportesForms(request.POST, instance=reportes)
		if form.is_valid():
			form.save()
		return redirect('reportes_listar')
	return render(request, 'sistema/reportes_form.html', {'form': form})

def reportes_eliminar(request, No_reporte):
	reportes = Reportes.objects.get(No_reporte = No_reporte)
	if request.method == 'POST':
		reportes.delete()
		return redirect('sistema/reportes_lista.html')
	return render(request, 'sistema/reportes_delete.html', {'reportes': reportes})

"""




class ReportesList(LoginRequiredMixin, ListView):
	"""docstring for ReportesList"""
	login_url = 'login'
	redirect_field_name = 'redirect_to'
	model = Reportes
	template_name = 'sistema/reportes_lista.html'
	paginate_by = 3


	def get_queryset(self):
		filter_val = self.request.GET.get('filter')
		new_context = Reportes.objects.filter(cliente__cliente=filter_val) | Reportes.objects.filter(trabajo_realizado=filter_val)
		print(new_context)
		return new_context
		
	def get_context_data(self, **kwargs):
		context = super(ReportesList, self).get_context_data(**kwargs)
		context['filter'] = self.request.GET.get('filter', 'give-default-value')
		
		return context

			

class ReportesCrear(LoginRequiredMixin, CreateView):
	"""vistas basadas en clases"""
	login_url = 'login'
	redirect_field_name = 'redirect_to'
	model = Reportes
	form_class = ReportesForms	
	template_name = 'sistema/reportes_form.html'
	success_url = reverse_lazy('reportes_listar')

class ReportesUpdate(LoginRequiredMixin, UpdateView):
	"""docstring for ReportesUpdate"""
	login_url = 'login'
	redirect_field_name = 'redirect_to'
	model = Reportes
	form_class = ReportesForms
	template_name = 'sistema/reportes_edit.html'
	success_url = reverse_lazy('reportes_listar')

class ReportesView(LoginRequiredMixin, UpdateView):
	"""docstring for ReportesUpdate"""
	login_url = 'login'
	redirect_field_name = 'redirect_to'
	model = Reportes
	form_class = ReportesForms
	template_name = 'sistema/reportes_view.html'
	success_url = reverse_lazy('reportes_listar')

class ReportesDelete(LoginRequiredMixin, DeleteView):
	"""docstring for ReportesDelete"""
	login_url = 'login'
	redirect_field_name = 'redirect_to'
	model = Reportes
	template_name = 'sistema/reportes_delete.html'
	success_url = reverse_lazy('reportes_listar')

