from django.shortcuts import render
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .forms import NewDepartamentoForm
from app.personas.models import Habilidades, Personas
from app.departamento.models import Departamento
from django.views.generic import (
    ListView,)

class ListAllDepartamentos(ListView):
    template_name = 'departamento/all_departamento.html'
    #model = Personas
    paginate_by = 4
    ordering = ('name',)
    context_object_name = 'departamentos'
    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')
        lista = Departamento.objects.filter(
            name__icontains=palabra_clave
        )
        return lista




class newDepartamentoView(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartamentoForm
    success_url = reverse_lazy('personas_app:success')

    def form_valid(self, form):

        dpto=Departamento(
            name=form.cleaned_data['departamento'],
            shor_name=form.cleaned_data['shorname'],
        )
        dpto.save()
        nombre = form.cleaned_data['nombre']
        apellidos = form.cleaned_data['apellidos']
        Personas.objects.create(
            name=nombre,
            last_name=apellidos,
            departamento=dpto,
            job='1',
            salario=0,
            cv='',
            


        )
       
        return super(newDepartamentoView, self).form_valid(form)