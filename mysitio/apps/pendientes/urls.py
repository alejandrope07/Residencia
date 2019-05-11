from django.urls import path,include
 
from apps.pendientes.views import  PendientesCrear, PendientesDelete, list_and_create


urlpatterns = [

    path('nuevo', list_and_create, name='pendientes_nuevo'),
    path('eliminar/<int:pk>/', PendientesDelete.as_view(), name='pendientes_eliminar')


   ]