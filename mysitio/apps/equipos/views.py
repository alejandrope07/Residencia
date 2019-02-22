from django.shortcuts import render, redirect

from django.http import HttpResponse


from apps.equipos.forms import EquiposForm
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