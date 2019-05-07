from principal.readCsv import readFile
from django.conf import settings
from principal.models import Usuario,Genero,Pelicula,Puntuacion,Etiqueta
import os
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    
    help = 'Populate from csv to database'
    
    def handle(self, *args, **options):
        moviesPath = os.path.join(settings.STATIC_ROOT,"csv/movies.csv")
        linksPath = os.path.join(settings.STATIC_ROOT,"csv/links.csv")
        ratingsPath = os.path.join(settings.STATIC_ROOT,"csv/ratings.csv")
        tagsPath = os.path.join(settings.STATIC_ROOT,"csv/tags.csv")
        
        print(readFile(moviesPath))
        
        generos = []
        for movie in readFile(moviesPath):
            generos.extend(movie["genres"])
            
            
        generos = set(generos)
        for genero in generos:
            generoObject = Genero(genero)
            generoObject.save()