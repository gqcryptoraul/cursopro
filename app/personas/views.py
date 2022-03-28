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

from .models import Personas

from .forms import PersonasForm


class ListAllPersonas(ListView):
    template_name = 'personas/list_all.html'
    #model = Personas
    paginate_by = 4
    ordering = ('full_name',)

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')
        lista = Personas.objects.filter(
            full_name__icontains=palabra_clave
        )
        return lista


class ListByAreaPersonas(ListView):
    template_name = 'personas/list_by_area.html'
    paginate_by = 5
    ordering = ('name',)

    def get_queryset(self):
        area = self.kwargs['area']
        lista = Personas.objects.filter(
            departamento__shor_name=area
        )
        return lista

# recuperar desde caja de texto


class ListPersonasByKeyword(ListView):
    template_name = 'personas/list_by_keyword.html'
    context_object_name = 'personas'
    paginate_by = 5
    ordering = ('name',)

    def get_queryset(self):
        area = self.request.GET.get('kword', '')
        lista = Personas.objects.filter(
            departamento__shor_name=area
        )
        return lista


class ListHabilidades(ListView):
    template_name = 'personas/list_habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):

        idtext = self.request.GET.get('id', '')
        if idtext == '' or idtext == '0':
            id = 0
            return []
        else:
            id = int(idtext)
            persona = Personas.objects.get(id=id)
            return persona.habilidades.all()


class PersonasDetailView(DetailView):
    model = Personas
    template_name = "personas/detail.html"
    context_object_name = 'persona'
    success_url = reverse_lazy('personas_app:all-personas')
    def get_context_data(self, **kwargs):
        context = super(PersonasDetailView, self).get_context_data(**kwargs)
        context['titulo'] = 'Detalle de la persona'
        return context


class SuccesView(TemplateView):
    template_name = "personas/success.html"


class PersonasCreateView(CreateView):
    
    template_name = "personas/create.html"
    model = Personas
    form_class = PersonasForm
    
    #fields =('__all__')
    success_url = reverse_lazy('personas_app:all-personas')

    def form_valid(self, form):

        persona = form.save(commit=False)
        persona.full_name = persona.name + ' ' + persona.last_name
        persona.save()
        return super(PersonasCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(PersonasCreateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Crear persona'
        return context


class PersonasUpdateView(UpdateView):
    model = Personas
    template_name = "personas/update.html"
    fields = ['name', 'last_name', 'correo', 'fec_nac', 'direccion',
              'departamento', 'job', 'habilidades', 'salario','full_name','cv','avatar']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('personas_app:all-personas')

    def post(self, request, *args, **kwargs):

        self.object = self.get_object()

        print(request.POST['name'] + ' ' + request.POST['name'])
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):

        persona = form.save(commit=False)
        persona.full_name = persona.name + ' ' + persona.last_name
        persona.save()
        return super(PersonasUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(PersonasUpdateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Update Personas'
        return context


class PersonasDeleteView(DeleteView):
    model = Personas
    template_name = "personas/delete.html"
    success_url = reverse_lazy('personas_app:all-personas')

    def get_context_data(self, **kwargs):
        context = super(PersonasDeleteView, self).get_context_data(**kwargs)
        context['titulo'] = 'Delete Personas'
        return context
