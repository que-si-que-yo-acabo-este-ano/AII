from django.contrib import admin
from principal.models import Usuario,Pelicula,Ocupacion,Categoria,Puntuacion

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Pelicula)
admin.site.register(Ocupacion)
admin.site.register(Categoria)
admin.site.register(Puntuacion)