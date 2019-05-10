from django.shortcuts import render
from principal.models import Pelicula
from django.shortcuts import render_to_response
# Create your views here.

def inicio(request):
    peliculas = Pelicula.objects.all()
    return render(request,'inicio.html',{'peliculas':peliculas})

def peliculas(request):
    peliculas = Pelicula.objects.all()
    print(peliculas[0].generos.all())
    return render(request,'peliculas.html',{'peliculas':peliculas})