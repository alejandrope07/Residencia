from django.urls import path,include
 
from apps.bitacora.views import  BitacoraCrear, BitacoraList


urlpatterns = [

    path('nuevo', BitacoraCrear.as_view(), name='bitacoras_nuevo'),
    path('lista', BitacoraList.as_view(), name='bitacoras_lista'),


   ]