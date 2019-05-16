from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.core import serializers
import json
from apps.bitacora.forms import BitacoraForm
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.bitacora.models import Bitacora
# Create your views here.
class BitacoraCrear(CreateView):
	"""vistas basadas en clases"""
	model = Bitacora
	form_class = BitacoraForm
	template_name = 'sistema/bitacora_form.html'
	success_url = reverse_lazy('reportes_listar')

class BitacoraList(LoginRequiredMixin, ListView):
	"""docstring for ReportesList"""
	login_url = 'login'
	redirect_field_name = 'redirect_to'
	model = Bitacora
	template_name = 'sistema/bitacora_lista.html'
	paginate_by = 5
