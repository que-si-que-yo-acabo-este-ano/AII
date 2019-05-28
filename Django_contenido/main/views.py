from django.shortcuts import render
from main.models import Artista, UsuarioEtiquetaArtista, UsuarioArtista, Usuario
from collections import Counter
from main import forms, models
import math
from math import sqrt

# Create your views here.

def artistTopTagsByUsersTest(artist):
    artistSearched = Artista.objects.get(idArtista= artist)
    allTagsObj = UsuarioEtiquetaArtista.objects.filter(artista= artistSearched)
    allTags = [obj.etiqueta for obj in allTagsObj]
    top4Tuples = Counter(allTags).most_common(4)
    return top4Tuples


def artistTopTagsByUsers(artist):
    artistSearched = Artista.objects.get(idArtista= artist)
    allTagsObj = UsuarioEtiquetaArtista.objects.filter(artista= artistSearched)
    allTags = [obj.etiqueta for obj in allTagsObj]
    top4Tuples = Counter(allTags).most_common(4)
    contentRecommendation(10)
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
    print('------- Inicio --------')
    for userArtistObj in UsuarioArtista.objects.filter(usuario= userObj):
        artists.remove(userArtistObj.artista)
        print('Dentro for remove artist')
    print('-------- Antes del for artistTagsList ---------')
    #tempCont = 0
    tagsForComparison = []
    artistsTagsList = []
    for artist in artists:
        tagsOfArtist = artistTopTagsByUsersTest(artist.idArtista)
        tagsForComparison.extend([x[0] for x in tagsOfArtist])
        artistsTagsList.append((artist,tagsOfArtist))
        #tempCont += 1
        #if tempCont%1000==0:
            #print('Dentro for artistTagsList' + str(tempCont))
    tagsForComparison = Counter(tagsForComparison).most_common()
    userTagsCount = userTopTags(user)
    userTags = [tagTuple[0] for tagTuple in userTagsCount]
    userTagsCountDict = dict(userTagsCount)
    
    tfUserVector = []
    for tagTop in tagsForComparison:
        if tagTop[0] in userTags:
            tfUserVector.append(userTagsCountDict.get(tagTop[0]))
        else:
            tfUserVector.append(0)
            
            
    #tfUserVector = [userTags.count(tag[0]) for tag in tagsForComparison] # Modificar
    nArtists = len(artistsTagsList)
    idfVector = [(numOcurrTag[0],math.log(nArtists/numOcurrTag[1])) for numOcurrTag in tagsForComparison]
#    userVector = []
#     print('-------- Antes del for userVector ---------')
#     for tag in idfVector:
#         print('Dentro for userVector')
#         if tag[0] in userTags:            
#             userVector.append(1.0)
#             #userVector.append(tag)
#         else:
#             userVector.append(0.0)
#             #userVector.append((tag[0],0.0))
#     print(userVector)
    userVector = [x*y for x,y in zip(tfUserVector,idfVector)] # Si asi funciona el for de encima sobra
    # TODO Lo mismo del userVector aplicarlo al artistVector
    print('-------- Antes del for artistsVectors ---------')
    tempCont = 0
    artistsVectors = []
    for artist in artistsTagsList:
        artistVector = []
        if tempCont%1000==0:
            print('Dentro for artistTagsList' + str(tempCont))
        for tag in idfVector:
            if tag[0] in artist[1][0]:
                artistVector.append(1.0)
                #artistVector.append(tag)
            else:
                artistVector.append(0.0)
                #artistVector.append((tag[0],0.0))
        artistsVectors.append((artist,artistVector))
        tempCont += 1
    
    simVector = []
    for artist in artistsVectors:
        top = sum([userVector[i] * artist[1][i] for i in range(len(userVector))])
        #print('Top ' + str(top))
        bottomLeft = sqrt(sum([pow(x,2) for x in userVector]))
        #print('BottomLeft ' + str(bottomLeft))
        bottomRight = sqrt(sum([pow(y,2) for y in artist[1]]))
        #print('BottomRight ' + str(bottomRight))
        sim = (top)/(bottomLeft)*(bottomRight)
        #print('-----')
        #print(sim)
        #print('-----')
        #print('------------------------------------------------')
        simVector.append((artist[0],sim))
    recommendedArtists = sorted(simVector, key=lambda x: -x[1])[:2]
    print(recommendedArtists)
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



def artistasUsuario(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = forms.artistasMasEscuchados(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            id = form.cleaned_data['id']
            artistasUsuarios = models.UsuarioArtista.objects.filter(usuario__idUsuario = id)
            print(artistasUsuarios)
            return render(request, 'artistasUsuario.html', {'form': form,'artistasUsuarios':artistasUsuarios,'id':id})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = forms.artistasMasEscuchados()
    return render(request, 'artistasUsuario.html', {'form': form})