from django.urls import path,include
from apps.usuarios.views import RegistroUsuarios, logout_view

urlpatterns = [
   path('registrar', RegistroUsuarios.as_view(), name='registro'),
   path('salir', logout_view, name='salir'),
]