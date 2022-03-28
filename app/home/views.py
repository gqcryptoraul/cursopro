from django.utils import timezone
from re import template
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import (
    ListView, 
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView,
      )


from .models import Test
from .forms import TestForm

class InicioView(TemplateView):
    template_name = 'home/inicio.html'

class PruebaView(TemplateView):
    template_name = 'home/prueba.html'

class ResumenFoundationView(TemplateView):
    template_name = 'home/resume_foundation.html'

class PruebaListView(ListView):
    template_name='home/list.html'
    context_object_name = 'listnumebers'
    queryset=['0','89','20','30']
    
class ListarTest(ListView):
    template_name = 'home/lista.html'
    model= Test
    context_object_name = 'lista'

class CrearTest(CreateView):
    template_name = 'home/add.html'
    model= Test
    #fields= ['titulo','subtitulo','cantidad']
    form_class= TestForm
    success_url = reverse_lazy('personas_app:success')
