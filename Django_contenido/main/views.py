from django.shortcuts import render
from main.models import Artista, UsuarioEtiquetaArtista
from collections import Counter

# Create your views here.






def artistTopTagsByUsers(artist):
    artistSearched = Artista.objects.get(nombre= artist)
    allTagsObj = UsuarioEtiquetaArtista.objects.filter(artista= artistSearched)
    allTags = [obj.etiqueta for obj in allTagsObj]
    top4Tuples = Counter(allTags).most_common(4)
    print(top4Tuples)
    return top4Tuples    