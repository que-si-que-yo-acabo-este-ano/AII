from django.shortcuts import render
from principal.models import Pelicula
from .forms import FilmsOfYearForm
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