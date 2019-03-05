from django.urls import path,include
from apps.reportes.views import index, reportes_view, reportes_lista, reportes_editar, reportes_eliminar, ReportesCrear, ReportesUpdate, ReportesList, ReportesDelete 



urlpatterns = [
    path('', index),

    path('nuevo', ReportesCrear.as_view()),
    path('listar', ReportesList.as_view(), name='reportes_listar'),
    path('editar/<int:No_reporte>/', reportes_editar, name='reporte_editar'),
    path('eliminar/<int:pk>/', ReportesDelete.as_view(), name='reporte_eliminar'),
]
