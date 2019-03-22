from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, ListView, DeleteView

from django.urls import reverse_lazy
from django.http import HttpResponse


from apps.reportes.forms import ReportesForms

from apps.reportes.models import Reportes, Empleados

# Create your views here.
def index(request):
	return render(request, 'sistema/index.html')

def reportes_view(request):
	if request.method == 'POST':
		form = ReportesForms(request.POST)
		if form.is_valid():
			form.save()

		return redirect('reportes_listar')

	else:
		form = ReportesForms()

	return render(request, 'sistema/reportes_form.html', {'form': form})

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



class ReportesList(ListView):
	"""docstring for ReportesList"""
	model = Reportes
	template_name = 'sistema/reportes_lista.html'
	paginate_by = 3
		

class ReportesCrear(CreateView):
	"""vistas basadas en clases"""
	model = Reportes
	form_class = ReportesForms
	template_name = 'sistema/reportes_form.html'
	success_url = reverse_lazy('reportes_listar')

class ReportesUpdate(UpdateView):
	"""docstring for ReportesUpdate"""
	model = Reportes
	form_class = ReportesForms
	template_name = 'sistema/reportes_form.html'
	success_url = reverse_lazy('sistema:reportes_listar')

class ReportesDelete(DeleteView):
	"""docstring for ReportesDelete"""
	model = Reportes
	template_name = 'sistema/reportes_delete.html'
	success_url = reverse_lazy('reportes_listar')

		