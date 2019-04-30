
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from apps.usuarios.forms import RegistroForm
from django.contrib.auth import logout
# Create your views here.

class RegistroUsuarios(CreateView):
	model = User
	template_name = "usuario/registrar.html"
	form_class = RegistroForm
	success_url = reverse_lazy('reportes_listar')

def logout_view(request):
    logout(request)
	
