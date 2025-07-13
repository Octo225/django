"""
URL configuration for prueba project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from inicio import views
from django.conf import settings
from registros import views as views_registros

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views_registros.registros, name="Principal"),
    path('contacto/', views.contacto, name="Contacto"),
    path('formulario/', views.formulario, name="Formulario"),
    path('ejemplo/', views.ejemplo, name="Ejemplo"),
    path('comentario/',views_registros.comentario, name="Comentario"),
    path('registrar/',views_registros.registrar,name="Registrar"),
    path('eliminarComentario/<int:id>/',views_registros.eliminarComentarioContacto, name="Eliminar"),
    path('consultas1/',views_registros.consultar1,name="Consultas"),
    path('consultas2/',views_registros.consultar2,name="Consultas"),
    path('consultas3/',views_registros.consultar3,name="Consultas"),
    path('consultas4/',views_registros.consultar4,name="Consultas"),
    path('consultas5/',views_registros.consultar5,name="Consultas"),
    path('consultas6/',views_registros.consultar6,name="Consultas"),
    path('consultas7/',views_registros.consultar7,name="Consultas"),
    path('comentario1/',views_registros.comentario1,name="comentarioConsultas"),
    path('comentario2/',views_registros.comentario2,name="comentarioConsultas"),
    path('comentario3/',views_registros.comentario3,name="comentarioConsultas"),
    path('comentario4/',views_registros.comentario4,name="comentarioConsultas"),
    path('comentario5/',views_registros.comentario5,name="comentarioConsultas"),
    path('subir/',views_registros.archivos,name="Subir"),











    path('formEditarComentario/<int:id>/',views_registros.consultarComentarioIndividual, name='ConsultaIndividual'),
    path('editarComentario/<int:id>/',views_registros.editarComentarioContacto,name='Editar'),


]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


