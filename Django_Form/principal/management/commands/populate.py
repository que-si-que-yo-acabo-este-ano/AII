from principal.readData import readMovieFile,readGenreFile,readUserFile,readRatingFile,\
    readOccupationFile
from django.conf import settings
from principal.models import Usuario,Pelicula,Puntuacion,Categoria,CategoriaPelicula,Ocupacion,Puntuacion
import os
from django.core.management.base import BaseCommand, CommandError
from datetime import datetime
from Django_Form.settings import STATIC_ROOT
from django.contrib.auth.models import User

class Command(BaseCommand):
    
    help = 'Populate from u.* to database'
    
    def handle(self, *args, **options):
        User.objects.create_superuser(username='admin', password='admin', email='admin@email.com')
        
        moviesPath = os.path.join(STATIC_ROOT,"data/u.item")
        usersPath = os.path.join(STATIC_ROOT,"data/u.user")
        genresPath = os.path.join(STATIC_ROOT,"data/u.genre")
        ratingsPath = os.path.join(STATIC_ROOT,"data/u.data")
        occupationsPath= os.path.join(STATIC_ROOT,"data/u.occupation")
        
        movies = readMovieFile(moviesPath)
        users = readUserFile(usersPath)
        genres = readGenreFile(genresPath)
        ratings = readRatingFile(ratingsPath)
        occupations = readOccupationFile(occupationsPath)
        
        generos = []
        for genre in genres:
            generos.append(Categoria(nombre = genre[0],idCategoria = int(genre[1])))
        Categoria.objects.bulk_create(generos)
        
        peliculas = []
        categoriasPeliculas = []
        for movie in movies:
            peliculas.append(Pelicula(idPelicula = int(movie[0]),titulo = movie[1],fechaDeEstreno = datetime.strptime(movie[2],"%d-%b-%Y"), imdbURL = movie[3]))
            for i,hasGenero in enumerate(movie[4]):
                if int(hasGenero):
                    if int(movie[0])-1<266:
                        categoriasPeliculas.append(CategoriaPelicula(idCategoria=generos[i],idPelicula=peliculas[int(movie[0])-1]))
                    else:
                        categoriasPeliculas.append(CategoriaPelicula(idCategoria=generos[i],idPelicula=peliculas[int(movie[0])-2]))
        Pelicula.objects.bulk_create(peliculas)
        CategoriaPelicula.objects.bulk_create(categoriasPeliculas)
        
        ocupaciones = []
        for occupation in occupations:
            ocupaciones.append(Ocupacion(nombre = occupation))
        Ocupacion.objects.bulk_create(ocupaciones)
        
        usuarios = []
        for user in users:
            usuarios.append(Usuario(idUsuario=int(user[0]),edad=int(user[1]),sexo=user[2],ocupacion = Ocupacion.objects.get(nombre=user[3]),codigoPostal=user[4]))
        Usuario.objects.bulk_create(usuarios)  
            
        puntuaciones = []
        ip = 0
        for rating in ratings:
            ip+=1
            if ip%1000==0:
                print(ip)
            if int(rating[1]) != 267:
                tiempo = datetime.fromtimestamp(int(rating[3]))
                puntuaciones.append(Puntuacion(idUsuario=Usuario.objects.get(idUsuario = int(rating[0])),idPelicula = Pelicula.objects.get(idPelicula = int(rating[1])), puntuacion = int(rating[2]), fecha=tiempo))
        Puntuacion.objects.bulk_create(puntuaciones)
            
            