from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin



# Create your views here.



class Inicio(LoginRequiredMixin, TemplateView):
	"""docstring for ReportesList"""
	login_url = 'login'
	redirect_field_name = 'redirect_to'

	template_name = 'sistema/inicio_form.html'