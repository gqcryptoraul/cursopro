# Generated by Django 4.0.3 on 2022-03-24 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departamento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Personas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('fec_nac', models.DateTimeField(blank=True, null=True, verbose_name='Fecha_Nac')),
                ('direccion', models.CharField(blank=True, max_length=200, null=True, verbose_name='Direccion')),
                ('correo', models.EmailField(blank=True, max_length=254, verbose_name='Correo')),
                ('job', models.CharField(choices=[('0', 'CONTADOR'), ('1', 'ADMINISTRADOR'), ('2', 'ECONOMISTA'), ('3', 'ASISTENTE')], max_length=1, verbose_name='Cargos')),
                ('salario', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='salario')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departamento.departamento')),
            ],
        ),
    ]
