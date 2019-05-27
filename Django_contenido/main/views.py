from django.shortcuts import render
from main.models import Artista, UsuarioEtiquetaArtista, UsuarioArtista
from collections import Counter

# Create your views here.






def artistTopTagsByUsers(artist):
    artistSearched = Artista.objects.get(nombre= artist)
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