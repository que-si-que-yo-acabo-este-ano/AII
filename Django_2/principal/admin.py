from django.contrib import admin
from principal.models import Bebida, Receta, Usuario, Genero, Pelicula, Etiqueta, Puntuacion

# Register your models here.

admin.site.register(Bebida)
admin.site.register(Receta)
admin.site.register(Usuario)
admin.site.register(Genero)
admin.site.register(Pelicula)
admin.site.register(Etiqueta)
admin.site.register(Puntuacion)