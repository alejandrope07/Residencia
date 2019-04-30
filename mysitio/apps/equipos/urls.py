from django.urls import path,include
from apps.equipos.views import index, validar_usuario, equipos_view, EquiposCrear, EquiposList, EquiposUpdate, EquiposDelete

urlpatterns = [
    path('', index),
    path('validar', validar_usuario),
    path('crear', EquiposCrear.as_view(), name='equipo_nuevo'),
    path('lista', EquiposList.as_view(), name='equipo_listar'),
    path('editar/<int:pk>/', EquiposUpdate.as_view(), name='equipo_editar'),
    path('eliminar/<int:pk>/', EquiposDelete.as_view(), name='equipo_eliminar'),

]
