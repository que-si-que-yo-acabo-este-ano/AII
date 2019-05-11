#encoding:utf-8
from django.shortcuts import render
from principal.models import Bebida, Pelicula, Genero
from django.shortcuts import render_to_response
# Create your views here.

def inicio(request):
    peliculas = Pelicula.objects.all()
    return render(request,'inicio.html',{'peliculas':peliculas})

def genres(request):
    genres = Genero.objects.all()
    return render(request,'genres.html',{'genres':genres})

def films_by_genre(request):
    genres = Genero.objects.all()
    films = Pelicula.objects.all()
    return render(request,'filmsByGenre.html',{'genres':genres,'films':films})
    

def peliculas(request):
    peliculas = Pelicula.objects.all()
    print(peliculas[0].generos.all())
    return render(request,'peliculas.html',{'peliculas':peliculas})