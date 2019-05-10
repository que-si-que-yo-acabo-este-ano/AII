from django.shortcuts import render
from principal.models import Bebida, Pelicula
from django.shortcuts import render_to_response
# Create your views here.

def lista_bebidas(request):
    bebidas = Bebida.objects.all()
    return render_to_response('lista_bebidas.html',{'lista':bebidas})

def inicio(request):
    peliculas = Pelicula.objects.all()
    return render(request,'inicio.html',{'peliculas':peliculas})