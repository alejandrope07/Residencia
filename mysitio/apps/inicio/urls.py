from django.urls import path,include
from apps.inicio.views import Inicio

urlpatterns = [
    path('', Inicio.as_view(), name="inicio"),


]
