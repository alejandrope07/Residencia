from django.shortcuts import render, redirect

from django.http import HttpResponse


from apps.reportes.forms import ReportesForms
# Create your views here.
def index(request):
	return render(request, 'sistema/index.html')

def reportes_view(request):
	if request.method == 'POST':
		form = ReportesForms(request.POST)
		if form.is_valid():
			form.save()

		return redirect(index)

	else:
		form = ReportesForms()

		return render(request, 'sistema/reportes_form.html', {'form': form})