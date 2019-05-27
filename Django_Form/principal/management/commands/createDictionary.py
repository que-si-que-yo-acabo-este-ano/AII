from django.core.management.base import BaseCommand, CommandError
from principal.models import Usuario,Pelicula,Puntuacion,Categoria,CategoriaPelicula,Ocupacion,Puntuacion
import shelve

class Command(BaseCommand):
    
    help = 'Persistent dictionaries from DB'
    
    def handle(self, *args, **options):
        dbDict = {"Usuarios": Usuario.objects.all()}
        usuarios = {}
        for usuario in Usuario.objects.all():
            puntuaciones = {}
            for puntuacion in Puntuacion.objects.filter(idUsuario = usuario.idUsuario):
#                 print(puntuacion.idPelicula)
                puntuaciones[Pelicula.objects.get(idPelicula = puntuacion.idPelicula.idPelicula).idPelicula] = puntuacion.puntuacion
            usuarios[usuario.idUsuario] = puntuaciones

        s = shelve.open('dicts.db')
        try:
            s['usuariosPuntuaciones'] = usuarios
        finally:
            s.close()

#         s = shelve.open('test_shelf.db')
#         try:
#             existing = s['key1']
#         finally:
#             s.close()
#         
#         print(existing)