from principal.readCsv import readFile
from django.conf import settings
from principal.models import Usuario,Genero,Pelicula,Puntuacion,Etiqueta
import os
from django.core.management.base import BaseCommand, CommandError
from datetime import datetime

class Command(BaseCommand):
    
    help = 'Populate from csv to database'
    
    def handle(self, *args, **options):
        moviesPath = os.path.join(settings.STATIC_ROOT,"csv/movies.csv")
        linksPath = os.path.join(settings.STATIC_ROOT,"csv/links.csv")
        ratingsPath = os.path.join(settings.STATIC_ROOT,"csv/ratings.csv")
        tagsPath = os.path.join(settings.STATIC_ROOT,"csv/tags.csv")
        
        movies = readFile(moviesPath)
        links = readFile(linksPath)
        ratings = readFile(ratingsPath)
        tags = readFile(tagsPath)
            
        for movie,link in zip(movies,links):
            tmdbId = link["tmdbId"]
            if tmdbId is "":
                tmdbId = 0
            pelicula = Pelicula(peliculaID = movie["movieId"], titulo = movie["title"],
                                imdbID = link["imdbId"],tmdbID = tmdbId)
            pelicula.save()
            for genre in movie["genres"]:
                genero,generoCreated = Genero.objects.get_or_create(genero = genre)
                if generoCreated:
                    genero.save()
                pelicula.generos.add(genero)
        ir=0        
        for rating in ratings:
            ir+=1
            usuario,usuarioCreated = Usuario.objects.get_or_create(usuarioID = rating["userId"])
            if usuarioCreated:
                usuario.save()
            tiempo = datetime.fromtimestamp(int(rating["timestamp"]))
            puntuacion = Puntuacion(usuarioID = Usuario.objects.get(usuarioID = rating["userId"]), peliculaID = Pelicula.objects.get(peliculaID = rating["movieId"])
                                    ,puntuacion = float(rating["rating"]), fecha = tiempo)
            puntuacion.save()
            if ir==10000:
                break
        it = 0
        for tag in tags:
            it+=1
            usuario,usuarioCreated = Usuario.objects.get_or_create(usuarioID = tag["userId"])
            if usuarioCreated:
                usuario.save()
            tiempo = datetime.fromtimestamp(int(tag["timestamp"]))
            etiqueta = Etiqueta(usuarioID = Usuario.objects.get(usuarioID = tag["userId"]), peliculaID = Pelicula.objects.get(peliculaID = tag["movieId"])
                                    ,etiqueta = tag["tag"], fecha = tiempo)
            etiqueta.save()
            if it==10000:
                break

            