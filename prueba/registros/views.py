from django.shortcuts import render
from .models import Alumnos
from .models import ComentarioContacto
from .forms import ComentarioContactoForm
from django.shortcuts import get_object_or_404

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


