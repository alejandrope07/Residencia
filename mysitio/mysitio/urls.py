"""mysitio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    path('admin/', admin.site.urls, name='admin1'),
    path('equipo/',include('apps.equipos.urls')),
    path('reportes/',include('apps.reportes.urls')),
    path('usuario/',include('apps.usuarios.urls')),
    path('clientes/',include('apps.clientes.urls')),
    path('bitacora/',include('apps.bitacora.urls')),
    path('inicio/',include('apps.inicio.urls')),
    path('pendientes/',include('apps.pendientes.urls')),
    path('', LoginView.as_view(template_name='sistema/index.html'), name="login"),
    path('reset/password_reset', PasswordResetView.as_view(template_name='registros/password_reset_form.html', html_email_template_name='registros/password_reset_email.html'), name='password_reset'), 

    path('reset/password_reset_done', PasswordResetDoneView.as_view(template_name='registros/password_reset_done.html'), 
    name='password_reset_done'),
    
    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', PasswordResetConfirmView.as_view(template_name='registros/password_reset_confirm.html'),
        name='password_reset_confirm'),

    path('reset/done', PasswordResetCompleteView.as_view(template_name='registros/password_reset_complete.html'),
    name='password_reset_complete'),
    

]
