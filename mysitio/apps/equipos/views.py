from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin

from apps.equipos.forms import EquiposForm
from apps.equipos.models import Equipo
# Create your views here.
def index(request):
	return render(request, 'sistema/index.html')

def equipos_view(request):
	if request.method == 'POST':
		form = EquiposForm(request.POST)
		if form.is_valid():
			form.save()

		return redirect(index)

	else:
		form = EquiposForm()

		return render(request, 'sistema/equipo_form.html', {'form': form})

def validar_usuario(request):
	if not request.user.is_authenticated:
		return redirect('login')


class EquiposList(LoginRequiredMixin, ListView):
	"""docstring for ReportesList"""
	login_url = 'login'
	redirect_field_name = 'redirect_to'
	model = Equipo
	template_name = 'sistema/equipos_lista.html'


class EquiposCrear(LoginRequiredMixin, CreateView):
	"""docstring for ReportesCrear"""
	login_url = 'login'
	redirect_field_name = 'redirect_to'
	model = Equipo
	form_class = EquiposForm
	template_name = 'sistema/equipo_form.html'
	success_url = reverse_lazy('equipo_listar')


class EquiposUpdate(LoginRequiredMixin, UpdateView):
	"""docstring for ReportesUpdate"""
	login_url = 'login'
	redirect_field_name = 'redirect_to'
	model = Equipo
	form_class = EquiposForm
	template_name = 'sistema/equipo_form.html'
	success_url = reverse_lazy('equipo_listar')

class EquiposView(LoginRequiredMixin, UpdateView):
	"""docstring for ReportesUpdate"""
	login_url = 'login'
	redirect_field_name = 'redirect_to'
	model = Equipo
	form_class = EquiposForm
	template_name = 'sistema/equipo_view.html'
	success_url = reverse_lazy('equipo_listar')

class EquiposDelete(LoginRequiredMixin, DeleteView):
	"""docstring for ReportesDelete"""
	login_url = 'login'
	redirect_field_name = 'redirect_to'
	model = Equipo
	template_name = 'sistema/equipo_delete.html'
	success_url = reverse_lazy('equipo_listar')
