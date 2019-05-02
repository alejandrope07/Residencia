from django.urls import path,include
from apps.reportes.views import index, inicio, validar_usuario, reportes_view, ReportesCrear, ReportesUpdate, ReportesList, ReportesDelete 
from apps.clientes.views import  CargarClientes


urlpatterns = [
    path('', index),
    path('', inicio, name='inicio_uno'),
    path('validar', validar_usuario),
    path('nuevo', ReportesCrear.as_view(), name='reportes_nuevo'),
    path('listar', ReportesList.as_view(), name='reportes_listar'),
    path('editar/<int:pk>/', ReportesUpdate.as_view(), name='reportes_editar'),
    path('eliminar/<int:pk>/', ReportesDelete.as_view(), name='reportes_eliminar'),
    path('editarc/', CargarClientes, name='cliente_editar'),
    
    
]
