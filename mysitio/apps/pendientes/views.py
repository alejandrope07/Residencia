from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.core import serializers
import json
from apps.pendientes.forms import PendientesForm
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.pendientes.models import Pendientes
from django.contrib.auth.decorators import login_required


# Create your views here.
class PendientesCrear(LoginRequiredMixin, CreateView):
	"""vistas basadas en clases"""
	login_url = 'login'
	redirect_field_name = 'redirect_to'
	model = Pendientes
	form_class = PendientesForm
	template_name = 'sistema/pendientes_form.html'
	success_url = reverse_lazy('reportes_listar')

class PendientesDelete(LoginRequiredMixin, DeleteView):
	"""docstring for ReportesDelete"""
	login_url = 'login'
	redirect_field_name = 'redirect_to'
	model = Pendientes
	template_name = 'sistema/pendientes_delete.html'
	success_url = reverse_lazy('pendientes_nuevo')

@login_required(login_url='login')
def list_and_create(request):
    form = PendientesForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
    
    objects = Pendientes.objects.all()
    return render(request, 'sistema/pendientes_form.html', {'objects': objects, 'form': form})