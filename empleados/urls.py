"""empleados URL Configuration

"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('',include('app.departamento.urls')),
    re_path('',include('app.personas.urls')),
    re_path('',include('app.home.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
