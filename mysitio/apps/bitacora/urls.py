from django.urls import path,include
 
from apps.bitacora.views import  BitacoraCrear


urlpatterns = [

    path('nuevo', BitacoraCrear.as_view(), name='bitacoras_nuevo'),


   ]