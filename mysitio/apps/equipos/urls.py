from django.urls import path,include
from apps.equipos.views import index, equipos_view, EquiposCrear, EquiposList, EquiposUpdate, EquiposDelete

urlpatterns = [
    path('', index),

    path('crear', EquiposCrear.as_view()),
    path('lista', EquiposList.as_view(), name='equipo_listar'),
    path('editar/<int:pk>/', EquiposUpdate.as_view(), name='equipo_editar'),
    path('eliminar/<int:pk>/', EquiposDelete.as_view(), name='equipo_eliminar'),

]
