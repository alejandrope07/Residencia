from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.core import serializers
import json
from apps.bitacora.forms import BitacoraForm

from apps.bitacora.models import Bitacora
# Create your views here.
class BitacoraCrear(CreateView):
	"""vistas basadas en clases"""
	model = Bitacora
	form_class = BitacoraForm
	template_name = 'sistema/bitacora_form.html'
	success_url = reverse_lazy('reportes_listar')