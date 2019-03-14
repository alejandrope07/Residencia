from django.urls import path,include
from apps.usuarios.views import RegistroUsuarios

urlpatterns = [
   path('registrar', RegistroUsuarios.as_view(), name='registro'),
]