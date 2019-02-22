from django.urls import path,include
from apps.reportes.views import index, reportes_view

urlpatterns = [
    path('', index),

    path('nuevo', reportes_view),
]
