from django.shortcuts import render
from main.models import Artista, UsuarioEtiquetaArtista, UsuarioArtista
from collections import Counter
from main import forms, models

# Create your views here.



def artistTopTagsByUsers(artist):
    artistSearched = Artista.objects.get(idArtista= artist)
    allTagsObj = UsuarioEtiquetaArtista.objects.filter(artista= artistSearched)
    allTags = [obj.etiqueta for obj in allTagsObj]
    top4Tuples = Counter(allTags).most_common(4)
    print(top4Tuples)
    return top4Tuples


def userTopTags(user):
    userArtists = UsuarioArtista.objects.filter(usuario= user)
    tuplesUserArtist = [(x.artista,x.tiempoEscucha) for x in userArtists]
    topUserArtists = sorted(tuplesUserArtist, key=lambda x: -x[1])[:5]
    


def contentRecommendation():
    pass


def artistasUsiario(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = forms.artistasMasEscuchados(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            id = form.cleaned_data['id']
            artistas = models.UsuarioArtista.objects.filter(usuario__idUsuario = id)
            print(artistas)
            return render(request, 'artistasUsiario.html', {'form': form,'artistas':artistas,'id':id})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = forms.artistasMasEscuchados()
    return render(request, 'artistasUsiario.html', {'form': form})