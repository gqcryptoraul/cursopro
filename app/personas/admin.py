from re import search
from django.contrib import admin
from .models import Personas,Habilidades
# Register your models here.

admin.site.register(Habilidades)

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'correo',
        'job',
        'departamento',
        'name_salary',
    )
    search_fields = ('name',)
    list_filter =('job','departamento',)
    filter_horizontal =('habilidades',)

    def name_salary(self, obj):
       
        return obj.name + ' ' + str(obj.salario)

admin.site.register(Personas,EmpleadoAdmin)