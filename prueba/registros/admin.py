from django.contrib import admin
from .models import Alumnos
from .models import Comentario
from .models import ComentarioContacto


# Register your models here.

class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display= ('matricula', 'nombre', 'carrera', 'turno',"created")
    search_fields=('matricula', 'nombre', 'carrera', 'turno')
    date_hierarchy= 'created'
    list_filter=('carrera','turno')

    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name="Usuarios").exists():
            return ('created', 'updated', 'matricula', 'carrera','turno')
        else:
            return('created', 'updated')

admin.site.register(Alumnos, AdministrarModelo)

class AdministrarComentarios(admin.ModelAdmin):
    readonly_fields = ('created','id')
    list_display= ('id', 'coment')
    search_fields=('id', 'created')
    date_hierarchy= ('created')

    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name="Comentarios").exists():
            return ('created', 'alumno')
        else:
            return('created')

admin.site.register(Comentario, AdministrarComentarios)

class AdministrarComentariosContacto(admin.ModelAdmin):
    ist_display = ('id', 'mensaje','created')
    earch_fields = ('id','created')
    ate_hierarchy = 'created'
    readonly_fields = ('created', 'id')
    
admin.site.register(ComentarioContacto, AdministrarComentariosContacto)