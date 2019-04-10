from django.urls import path,include
from apps.clientes.views import ClientesCrear, EmpleadosCrear, ClienteEditar


urlpatterns = [
    path('nuevo', ClientesCrear.as_view(), name='clientes_nuevo'),
    path('nuevoe', EmpleadosCrear.as_view(), name='empleados_nuevo'),
   



    ]