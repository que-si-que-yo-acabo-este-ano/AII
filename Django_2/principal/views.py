from django.shortcuts import render
from principal.models import Pelicula, Genero
from django.shortcuts import render_to_response
from django.template.context_processors import request
from principal import forms
from django.http.response import HttpResponseRedirect

# Create your views here.

def inicio(request):
    peliculas = Pelicula.objects.all()
    return render(request,'inicio.html',{'peliculas':peliculas})

def peliculas(request):
    peliculas = Pelicula.objects.all()
    print(peliculas[0].generos.all())
    return render(request,'peliculas.html',{'peliculas':peliculas})

def generos(request):
    generos = Genero.objects.all()
    print(generos)
    return render(request,'generos.html',{'generos':generos})

def generosPorPeliculas(request):
    peliculas = Pelicula.objects.all()
    print(peliculas[0].generos.all())
    return render(request,'generosPorPelicula.html',{'peliculas':peliculas})

def nuevaPeli(request):
    if request.method == 'POST':
        form = forms.PeliculaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('../')
    else:
        form = forms.PeliculaForm()
        
    return render(request,'nuevaPeli.html',{'form':form})