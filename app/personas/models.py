
from distutils.command.upload import upload
from enum import unique
from django.db import models

from app.departamento.models import Departamento
from ckeditor.fields import RichTextField

class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)

    class Meta:
        verbose_name= 'Habilidad'
        verbose_name_plural='Habilidad Personas'
      

    def __str__(self):
        return str(self.id) + '-' + self.habilidad 

# Create your models here.
class Personas(models.Model):

    JOB_CHOICES = (
        ('0', 'CONTADOR'),
        ('1', 'ADMINISTRADOR'),
        ('2', 'ECONOMISTA'),
        ('3', 'ASISTENTE'),

    )
    class Meta:
        verbose_name= 'Personas'
        verbose_name_plural='Persona'
        ordering = ['name']
        unique_together =('name','correo')

    name = models.CharField('Nombre',max_length=100)
    last_name = models.CharField('Apellido',max_length=100, null=True, blank=True)
    full_name = models.CharField('Nombre Completo',max_length=200, blank=True, null=True)
    #departamento = models.OneToOneField(Departamento, null=True, blank=True, on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    fec_nac = models.DateTimeField('Fecha_Nac',blank=True, null=True)
    direccion = models.CharField('Direccion', max_length=200, null=True, blank=True)
    correo = models.EmailField('Correo',blank=True)
    job = models.CharField('Cargos', max_length=1, choices=JOB_CHOICES)
    salario = models.DecimalField('salario', max_digits=10, decimal_places=2)
    habilidades = models.ManyToManyField(Habilidades,blank=True)
    cv = RichTextField()
    avatar = models.ImageField(upload_to='personas', null=True, blank=True)

    def __str__(self):
        return str(self.id) + '-' + self.name 
