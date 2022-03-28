from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
  
    path('prueba/', views.PruebaView.as_view()),
    path('list/', views.PruebaListView.as_view()),
    path('lista/', views.ListarTest.as_view()),
    path('add/', views.CrearTest.as_view()),
    path('resume-foundation/', views.ResumenFoundationView.as_view(),name='resume-foundation'),
    path('', views.InicioView.as_view(),name='inicio'),
 ]