from django.shortcuts import render
from principal.models import Pelicula
from principal import recommendations
from .forms import FilmsOfYearForm, UserInputForm
from django.db.models.functions import ExtractYear
import datetime

# Create your views here.


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
            dateshow = datetime.datetime(showyear, 1, 1)
            films = Pelicula.objects.filter(fechaDeEstreno__year = showyear)
            return render(request, 'filmsOfYear.html', {'form': form, 'showyear':showyear, 'films':films})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = FilmsOfYearForm()
    return render(request, 'filmsOfYear.html', {'form': form})


dic = {'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
 'Just My Luck': 3.0},
'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5, 
 'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0}, 
'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
 'Superman Returns': 3.5, 'The Night Listener': 4.0},
'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
 'You, Me and Dupree': 2.5},
'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0, 
 'Superman Returns': 3.0, 'The Night Listener': 3.0, 'You, Me and Dupree': 2.0}, 
'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
 'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
'Toby': {'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Returns':4.0}}

allFilms = ['Lady in the Water', 'Snakes on a Plane', 'Just My Luck', 'Superman Returns', 'You, Me and Dupree', 'The Night Listener']

def rec_not_rated_users(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserInputForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            user = form.cleaned_data['user'] # TODO Se supone que hay que hacerlo con userId no con el nombre
            recommendedFilms = recommendations.getRecommendations(dic,user)
            top2 = sorted(recommendedFilms, key=lambda x: -x[0])[:2]
            return render(request, 'recNotRated1.html', {'form': form, 'user':user, 'films':top2, 'prueba':recommendedFilms})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserInputForm()
    return render(request, 'recNotRated1.html', {'form': form})
