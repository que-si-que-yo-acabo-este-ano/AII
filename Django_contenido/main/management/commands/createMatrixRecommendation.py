from django.core.management.base import BaseCommand, CommandError
from main.models import Usuario, Etiqueta, Artista, UsuarioEtiquetaArtista
import math
from math import sqrt
from collections import Counter
import shelve

class Command(BaseCommand):
    
    help = 'PersistentData tf idf'
    
    def handle(self, *args, **options):
        def artistTopTagsByUsers(artist):
            artistSearched = Artista.objects.get(idArtista= artist)
            allTagsObj = UsuarioEtiquetaArtista.objects.filter(artista= artistSearched)
            allTags = [obj.etiqueta for obj in allTagsObj]
            top4Tuples = Counter(allTags).most_common(4)
            return top4Tuples
        
        artists = [x for x in Artista.objects.all()]
        tagsForComparison = []
        artistsTagsList = []
        for artist in artists:
            tagsOfArtist = [tagTuple[0] for tagTuple in artistTopTagsByUsers(artist.idArtista)]
            tagsForComparison.extend(tagsOfArtist)
            artistsTagsList.append((artist,tagsOfArtist))
        tagsForComparison = Counter(tagsForComparison).most_common()
        
        
        nArtists = len(artistsTagsList)
        idfVector = [(numOcurrTag[0],math.log(nArtists/numOcurrTag[1])) for numOcurrTag in tagsForComparison]
        
        artistsVectors = []
        for artist in artistsTagsList:
            artistVector = []
            for tag in idfVector:
                if tag[0] in artist[1]:
                    artistVector.append(1.0)
                    #artistVector.append(tag)
                else:
                    artistVector.append(0.0)
                    #artistVector.append((tag[0],0.0))
        artistsVectors.append((artist,artistVector))
        
        s = shelve.open('recommendation.db')
        try:
            s['tagsForComparison'] = tagsForComparison
            s['artistsTagList'] = artistsTagsList
            s['idfVector'] = idfVector
            s['artistsVectors'] = artistsVectors
        finally:
            s.close()