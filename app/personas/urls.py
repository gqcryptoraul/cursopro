from django.contrib import admin
from django.urls import path

from . import views

app_name = 'personas_app'
urlpatterns = [
  
    path('listar-all-personas/', views.ListAllPersonas.as_view(),name ='all-personas'),
    path('list-by-area/<area>/', views.ListByAreaPersonas.as_view(),name ='list-by-area'),
    path('find-personas/', views.ListPersonasByKeyword.as_view(),name ='find-personas'),
    path('habilidades/', views.ListHabilidades.as_view()),
    path('ver-detail/<pk>/', views.PersonasDetailView.as_view(),name='ver-detail'),
    path('add-personas/', views.PersonasCreateView.as_view(),name='add-personas'),
    path('success/', views.SuccesView.as_view(),name='success'),
    path('update-personas/<pk>/', views.PersonasUpdateView.as_view(),name='update-personas'),
    path('delete-personas/<pk>/', views.PersonasDeleteView.as_view(),name='delete-personas'),
    
   
 ]