from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView

from django.urls import reverse_lazy
from django.http import HttpResponse


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

class EquiposCrear(CreateView):
	"""docstring for ReportesCrear"""
	model = Equipo
	form_class = EquiposForm
	template_name = 'sistema/equipo_form.html'
	success_url = reverse_lazy(index)

class EquiposList(ListView):
	"""docstring for ReportesList"""
	model = Equipo
	template_name = 'sistema/equipos_lista.html'