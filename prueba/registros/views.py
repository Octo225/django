from django.shortcuts import render
from .models import Alumnos
from .models import ComentarioContacto
from .forms import ComentarioContactoForm
from django.shortcuts import get_object_or_404
from .models import Archivos
from .forms import FormArchivos
from django.contrib import messages
import datetime


def registros(request):
    alumnos=Alumnos.objects.all()
    return render(request,"registros/principal.html",{'alumnos':alumnos})

def registrar(request):
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST)
        if form.is_valid(): 
        
            form.save() 
            return comentario(request)

    form = ComentarioContactoForm()
    return render(request,'registros/contacto.html',{'form': form})

def comentario(request):
    comentarios=ComentarioContacto.objects.all()
    return render(request,"registros/comentario.html",{'comentarios':comentarios})

def contacto(request):
    return render(request,"registros/contacto.html")

def eliminarComentarioContacto(request, id, confirmacion='registros/confirmarEliminacion.html'):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    if request.method=='POST':
            comentario.delete()
            comentarios=ComentarioContacto.objects.all()
            return render(request,"registros/comentario.html",{'comentarios':comentarios})
    return render(request, confirmacion, {'object':comentario})

def consultar1(request):
     alumnos=Alumnos.objects.filter(carrera="TI")
     return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar2(request):
     alumnos=Alumnos.objects.filter(carrera="TI").filter(turno="Matutino")
     return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar3(request):
     alumnos=Alumnos.objects.only("matricula", "nombre","carrera","turno","imagen")
     return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar4(request):
     alumnos=Alumnos.objects.filter(turno__contains="Vesp")
     return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar5(request):
     alumnos=Alumnos.objects.filter(nombre__in=["Juan","Ana"])
     return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar6(request):
     fechaInicio= datetime.date(2025,6,20)
     fechaFIn= datetime.date(2025,7,11)
     alumnos=Alumnos.objects.filter(created__range=(fechaInicio,fechaFIn))
     return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar7(request):
     alumnos=Alumnos.objects.filter(comentario__coment__contains="prueba")
     return render(request,"registros/consultas.html",{'alumnos':alumnos})


def consultarComentarioIndividual(request, id):
    comentario=ComentarioContacto.objects.get(id=id)
    return render(request,"registros/formEditarComentario.html",{'comentario':comentario})


def editarComentarioContacto(request, id):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    form = ComentarioContactoForm(request.POST, instance=comentario)

    if form.is_valid():
        form.save() 
        comentarios=ComentarioContacto.objects.all()
        return render(request,"registros/comentario.html",{'comentarios':comentarios})
    else:
        return render(request,"registros/formEditarComentario.html",{'comentario':comentario})
    
def comentario1(request):
     fechaInicio= datetime.date(2025,7,4)
     fechaFin= datetime.date(2025,7,10)
     comentarios=ComentarioContacto.objects.filter(created__range=(fechaInicio,fechaFin))
     return render(request,"registros/comentarioConsultas.html",{'comentarios':comentarios})

def comentario2(request):
     comentarios=ComentarioContacto.objects.filter(mensaje__contains="cambio")
     return render(request,"registros/comentarioConsultas.html",{'comentarios':comentarios})

def comentario3(request):
     comentarios=ComentarioContacto.objects.filter(usuario__contains="Pedro")
     return render(request,"registros/comentarioConsultas.html",{'comentarios':comentarios})

def comentario4(request):
     comentarios=ComentarioContacto.objects.only("mensaje")
     return render(request,"registros/comentarioConsultas.html",{'comentarios':comentarios})

def comentario5(request):
     fechaInicio= datetime.date(2025,7,10)
     comentarios=ComentarioContacto.objects.filter(created__gte=(fechaInicio))
     return render(request,"registros/comentarioConsultas.html",{'comentarios':comentarios})

def archivos(request):
    if request.method == 'POST':
        form = FormArchivos(request.POST, request.FILES)
        if form.is_valid():
            titulo = request.POST['titulo']
            descripcion = request.POST['descripcion']
            archivo = request.FILES['archivo']
            insert = Archivos(titulo=titulo, descripcion=descripcion, archivo=archivo)
            insert.save()
            return render(request, "registros/archivos.html")
        else:
            messages.error(request, "Error al procesar el formulario")
    else:
         return render(request,"registros/archivos.html",{'archivo':Archivos})