#encoding:utf-8
from django.shortcuts import render
from principal.models import Pelicula, Genero, Puntuacion
from django.shortcuts import render_to_response
from django.template.defaultfilters import length
from _decimal import Decimal
from django.http import HttpResponseRedirect
from .forms import FilmsOfYearForm
# Create your views here.

def inicio(request):
    peliculas = Pelicula.objects.all()
    return render(request,'inicio.html',{'peliculas':peliculas})

def genres(request):
    genres = Genero.objects.order_by('genero').all()
    return render(request,'genres.html',{'genres':genres})

def films_by_genre(request):
    genres = Genero.objects.order_by('genero').all()
    films = Pelicula.objects.order_by('titulo').all()
    return render(request,'filmsByGenre.html',{'genres':genres,'films':films})
    
def peliculas(request):
    peliculas = Pelicula.objects.all()
    print(peliculas[0].generos.all())
    return render(request,'peliculas.html',{'peliculas':peliculas})

def top5_films(request):
    filmsWithRating = []
    films = Pelicula.objects.all()
    top5 = []
    for film in films:
        total = 0.0
        ratings = Puntuacion.objects.filter(peliculaID=film.peliculaID)
        for rating in ratings:
            #top5.append(rating)
            total += float(rating.puntuacion)
        if length(ratings) != 0:
            filmsWithRating.append((film.titulo,total/length(ratings)))
    top5 = sorted(filmsWithRating, key=lambda x: -x[1])[:500]
    return render(request, 'top5.html', {'top5':top5})

def films_of_year(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FilmsOfYearForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            showyear = form.cleaned_data['year']
            title = form.cleaned_data['title']
            films = Pelicula.objects.filter(titulo__icontains=title)
            return render(request, 'filmsOfYear.html', {'form': form, 'showyear':showyear,'films':films})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = FilmsOfYearForm()
    return render(request, 'filmsOfYear.html', {'form': form})