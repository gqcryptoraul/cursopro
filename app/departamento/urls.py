from django.contrib import admin
from django.urls import path


from . import views
app_name = 'departamento_app'
urlpatterns = [
  
    path('new-departamento/', views.newDepartamentoView.as_view(),name='new-departamento'),
    path('all-departamento/', views.ListAllDepartamentos.as_view(),name='all-departamento'),
    
 ]