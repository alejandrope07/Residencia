from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.core import serializers
import json
from apps.pendientes.forms import PendientesForm

from apps.pendientes.models import Pendientes
# Create your views here.
class PendientesCrear(CreateView):
	"""vistas basadas en clases"""
	model = Pendientes
	form_class = PendientesForm
	template_name = 'sistema/pendientes_form.html'
	success_url = reverse_lazy('reportes_listar')



def list_and_create(request):
    form = PendientesForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()

    
    objects = Pendientes.objects.all()
    return render(request, 'sistema/pendientes_form.html', {'objects': objects, 'form': form})