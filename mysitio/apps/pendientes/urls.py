from django.urls import path,include
 
from apps.pendientes.views import  PendientesCrear, list_and_create


urlpatterns = [

    path('nuevo', list_and_create, name='pendientes_nuevo'),


   ]