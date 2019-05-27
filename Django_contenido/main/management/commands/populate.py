import os
from Django_contenido.settings import STATIC_ROOT
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from main.readData import readFile,readUserArtistTagFile
from main.models import Usuario, Etiqueta, Artista, UsuarioArtista, UsuarioEtiquetaArtista

class Command(BaseCommand):
    
    help = 'Populate from .dat to database'
    
    def handle(self, *args, **options):
        User.objects.create_superuser(username='admin', password='admin', email='admin@email.com')
    
        tagPath = os.path.join(STATIC_ROOT,"data/tags.dat")
        artistPath = os.path.join(STATIC_ROOT,"data/artists.dat")
        userArtistsPath = os.path.join(STATIC_ROOT,"data/user_artists.dat")
        userTaggedartistsPath = os.path.join(STATIC_ROOT,"data/user_taggedartists.dat")
        
        tags = readFile(tagPath)
        artists = readFile(artistPath)
        userArtists = readFile(userArtistsPath)
        userTaggedartists = readUserArtistTagFile(userTaggedartistsPath)
        etiquetas = []
        for tag in tags:
            etiquetas.append(Etiqueta(idTag=tag[0],tagValue=tag[1]))
        Etiqueta.objects.bulk_create(etiquetas)
         
        artistas = []
        for artist in artists:
            if len(artist)>3:
                artistas.append(Artista(idArtista=artist[0],nombre=artist[1],url=artist[2],pictureUrl=artist[3]))
            else:
                artistas.append(Artista(idArtista=artist[0],nombre=artist[1],url=artist[2]))
        Artista.objects.bulk_create(artistas)
         
        usuarioArtistas = []
        for userArtist in userArtists:
            usuario,usuarioCreated = Usuario.objects.get_or_create(idUsuario = userArtist[0])
            if usuarioCreated:
                usuario.save()
            artista = Artista.objects.get(idArtista=userArtist[1])
            usuarioArtistas.append(UsuarioArtista(usuario= usuario,artista = artista,tiempoEscucha = userArtist[2]))
        UsuarioArtista.objects.bulk_create(usuarioArtistas)
          
        usuarioEtiquetaArtistas = []
        for userTaggedartist in userTaggedartists:
            usuario = Usuario.objects.get(idUsuario=userTaggedartist[0])
            artista = Artista.objects.filter(idArtista=userTaggedartist[1]).first()
            etiqueta = Etiqueta.objects.get(idTag=userTaggedartist[2])
            usuarioEtiquetaArtistas.append(UsuarioEtiquetaArtista(usuario=usuario,artista=artista,etiqueta=etiqueta,dia=userTaggedartist[3],mes=userTaggedartist[4],anyo=userTaggedartist[5]))
        UsuarioEtiquetaArtista.objects.bulk_create(usuarioEtiquetaArtistas)    
          
             
        