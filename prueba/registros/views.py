from django.shortcuts import render, redirect
from .models import Alumnos
from .models import ComentarioContacto
from .forms import ComentarioContactoForm

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


