from django.contrib import admin

# Register your models here.
from django.contrib import admin

from apps.clientes.models import Clientes, Empleados, Lugar

# Register your models here.
admin.site.register(Clientes)
admin.site.register(Empleados)
admin.site.register(Lugar)
