from django.db import models

# Create your models here.
class Departamento(models.Model):
    name = models.CharField('Nombre',max_length=100)
    shor_name = models.CharField('Nombre Corto',max_length=50, unique=True)
    anulate = models.BooleanField('Anulada',default=False)


    class Meta:
        verbose_name= 'Departamento'
        verbose_name_plural='Dpto'
    def __str__(self):
        return str(self.id) + '-' + self.name + '-' + self.shor_name