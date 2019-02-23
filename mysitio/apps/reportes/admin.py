from django.contrib import admin

from apps.reportes.models import Empleados, Reportes

# Register your models here.
admin.site.register(Empleados)
admin.site.register(Reportes)