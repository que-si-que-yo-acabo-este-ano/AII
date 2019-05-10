from principal.readCsv import readFile
from django.conf import settings
from principal.models import Usuario,Genero,Pelicula,Puntuacion,Etiqueta
import os
from django.core.management.base import BaseCommand, CommandError
from datetime import datetime
from django.contrib.auth.models import User

class Command(BaseCommand):
    
    help = 'Populate from csv to database'
    
    def handle(self, *args, **options):
#         Etiqueta.objects.all().delete()
#         Puntuacion.objects.all().delete()
#         Pelicula.objects.all().delete()
#         Genero.objects.all().delete()
#         Usuario.objects.all().delete()
#         print("borrado")
        User.objects.create_superuser(username='admin', password='admin', email='admin@email.com')
        
        moviesPath = os.path.join(settings.STATIC_ROOT,"csv/movies.csv")
        linksPath = os.path.join(settings.STATIC_ROOT,"csv/links.csv")
        ratingsPath = os.path.join(settings.STATIC_ROOT,"csv/ratings.csv")
        tagsPath = os.path.join(settings.STATIC_ROOT,"csv/tags.csv")
        
        movies = readFile(moviesPath)
        links = readFile(linksPath)
        ratings = readFile(ratingsPath)
        tags = readFile(tagsPath)
            
        peliculas = []
        generos = []
        
        i = 0
        for movie,link in zip(movies,links):
            i+=1
            tmdbId = link["tmdbId"]
            if tmdbId is "":
                pelicula = Pelicula(peliculaID = movie["movieId"], titulo = movie["title"],
                                imdbID = link["imdbId"])
            else:
                pelicula = Pelicula(peliculaID = movie["movieId"], titulo = movie["title"],
                                imdbID = link["imdbId"],tmdbID = tmdbId)

            genres = []
            for genre in movie["genres"]:
                genero,generoCreated = Genero.objects.get_or_create(genero = genre)
                if generoCreated:
                    genero.save()
                genres.append(genero)
            generos.append(genres)
#                 pelicula.generos.add(genero)
            if i%1000==0:
                print(i)
            peliculas.append(pelicula)
        Pelicula.objects.bulk_create(peliculas)
        ig = 0
        for pelicula,generosPelicula in zip(peliculas,generos):
            ig+=1
            if ig%100==0:
                print(ig)
            pelicula.generos.add(*generosPelicula)
            
        ir=0
        puntuaciones = []
        for rating in ratings:
            ir+=1
            usuario,usuarioCreated = Usuario.objects.get_or_create(usuarioID = rating["userId"])
            if usuarioCreated:
                usuario.save()
            tiempo = datetime.fromtimestamp(int(rating["timestamp"]))
            puntuacion = Puntuacion(usuarioID = Usuario.objects.get(usuarioID = rating["userId"]), peliculaID = Pelicula.objects.get(peliculaID = rating["movieId"])
                                    ,puntuacion = float(rating["rating"]), fecha = tiempo)
            puntuaciones.append(puntuacion)
            if ir%1000==0:
                print(ir)
        Puntuacion.objects.bulk_create(puntuaciones)
    
        it = 0
        etiquetas = []
        for tag in tags:
            it+=1
            usuario,usuarioCreated = Usuario.objects.get_or_create(usuarioID = tag["userId"])
            if usuarioCreated:
                usuario.save()
            tiempo = datetime.fromtimestamp(int(tag["timestamp"]))
            etiqueta = Etiqueta(usuarioID = Usuario.objects.get(usuarioID = tag["userId"]), peliculaID = Pelicula.objects.get(peliculaID = tag["movieId"])
                                    ,etiqueta = tag["tag"], fecha = tiempo)
            etiquetas.append(etiqueta)
            if it%100==0:
                print(it)
        Etiqueta.objects.bulk_create(etiquetas)
            