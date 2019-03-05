from django.urls import path,include
from apps.equipos.views import index, equipos_view, EquiposCrear, EquiposList

urlpatterns = [
    path('', index),

    path('crear', EquiposCrear.as_view()),
    path('lista', EquiposList.as_view()),
]
