from django.urls import path,include
from apps.equipos.views import index, equipos_view

urlpatterns = [
    path('', index),

    path('crear', equipos_view),
]
