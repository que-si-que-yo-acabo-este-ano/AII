from django.contrib import admin
from principal.models import Usuario, Genero, Pelicula, Etiqueta, Puntuacion

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Genero)
admin.site.register(Pelicula)
admin.site.register(Etiqueta)
admin.site.register(Puntuacion)