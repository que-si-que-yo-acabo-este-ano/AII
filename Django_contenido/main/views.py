from django.shortcuts import render
from main.models import Artista, UsuarioEtiquetaArtista, UsuarioArtista, Usuario
from collections import Counter
from main import forms, models
import math

# Create your views here.



def artistTopTagsByUsers(artist):
    artistSearched = Artista.objects.get(idArtista= artist)
    allTagsObj = UsuarioEtiquetaArtista.objects.filter(artista= artistSearched)
    allTags = [obj.etiqueta for obj in allTagsObj]
    top4Tuples = Counter(allTags).most_common(4)
    return top4Tuples


def userTopTags(user):
    userObj = Usuario.objects.get(idUsuario= user)
    userArtists = UsuarioArtista.objects.filter(usuario= userObj)
    tuplesUserArtist = [(x.artista,x.tiempoEscucha) for x in userArtists]
    topUserArtists = sorted(tuplesUserArtist, key=lambda x: -x[1])[:5]
    allTags = []
    for artist in topUserArtists:
        allTags.extend([obj.etiqueta for obj in UsuarioEtiquetaArtista.objects.filter(artista= artist[0])])
    top4Tuples = Counter(allTags).most_common(4)
    return top4Tuples


def contentRecommendation(user):
    userObj = Usuario.objects.get(idUsuario= user)
    artists = [x for x in Artista.objects.all()]
    for userArtistObj in UsuarioArtista.objects.filter(usuario= userObj):
        artists.remove(userArtistObj.artista)
    tagsForComparison = []
    artistsTags = []
    for artist in artists:
        tagsOfArtist = [tagTuple[0] for tagTuple in artistTopTagsByUsers(artist)]
        tagsForComparison.extend(tagsOfArtist)
        artistsTags.append((artist,tagsOfArtist))
    tagsForComparison = Counter(tagsForComparison)
    userTags = [tagTuple[0] for tagTuple in userTopTags(user)]
    
    tfUserVector = [userTags.count(tag[0]) for tag in tagsForComparison]
    
    nArtists = len(artists)
    idfVector = [(numOcurrTag[0],math.log(nArtists/numOcurrTag[1])) for numOcurrTag in tagsForComparison]
    userVector = []
    for tag in idfVector:
        if tag[0] in userTags:
            userVector.append(tag)
        else:
            userVector.append(tag[0],0.0)
    artistsVectors = []
    for artist in artistsTags:
        artistVector = []
        for tag in idfVector:
            if tag[0] in artist[1]:
                artistVector.append(tag)
            else:
                artistVector.append(tag[0],0.0)
        artistsVectors.append((artist,artistVector))
        
    # Hallar similitud entre userVector y cada uno de los artistsVectors
                
            
        


def artistTags(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = forms.artistTopTags(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            id = form.cleaned_data['id']
            topTags = artistTopTagsByUsers(id)
            return render(request, 'artistTopTags.html', {'form': form,'topTags':topTags,'id':id})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = forms.artistTopTags()
    return render(request, 'artistTopTags.html', {'form': form})



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
            return render(request, 'artistasUsiario.html', {'form': form,'artistas':artistas,'id':id})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = forms.artistasMasEscuchados()
    return render(request, 'artistasUsiario.html', {'form': form})
