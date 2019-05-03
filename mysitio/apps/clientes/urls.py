from django.urls import path,include
from apps.clientes.views import ClientesCrear, EmpleadosCrear, ClienteEditar, EmpleadosList, ClientesList, ClienteView, ClienteDelete


urlpatterns = [
    path('nuevo', ClientesCrear.as_view(), name='clientes_nuevo'),
    path('nuevoe', EmpleadosCrear.as_view(), name='empleados_nuevo'),
    path('listaemp', EmpleadosList.as_view(), name='empleados_lista'),
    path('listacli', ClientesList.as_view(), name='clientes_lista'),
    path('ver/<int:pk>/', ClienteView.as_view(), name='clientes_ver'),
    path('editar/<int:pk>/', ClienteEditar.as_view(), name='clientes_editar'),
    path('eliminar/<int:pk>/', ClienteDelete.as_view(), name='clientes_eliminar'),
   



    ]