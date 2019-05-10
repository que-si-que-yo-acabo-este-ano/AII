#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User
from unittest.util import _MAX_LENGTH

class Usuario(models.Model):
    usuarioID = models.IntegerField(primary_key=True)

class Genero(models.Model):
    genero = models.TextField(primary_key=True)

class Pelicula(models.Model):
    peliculaID = models.IntegerField(primary_key = True)
    titulo = models.CharField(max_length=100)    
    imdbID = models.IntegerField()
    tmdbID = models.IntegerField(null=True)
    puntuaciones = models.ManyToManyField(
        Usuario,
        through="Puntuacion")
    etiquetas = models.ManyToManyField(
        Usuario,
        through="Etiqueta",
        related_name="etiquetas")
    generos = models.ManyToManyField(Genero)
    def __str__(self):
        return self.titulo
     
class Etiqueta(models.Model):
    usuarioID = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    peliculaID = models.ForeignKey(Pelicula,on_delete=models.CASCADE)
    etiqueta = models.TextField()
    fecha = models.DateTimeField()
     
    def __str__(self):
        return self.etiqueta
     
class Puntuacion(models.Model):
    usuarioID = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    peliculaID = models.ForeignKey(Pelicula,on_delete=models.CASCADE)
    puntuacion = models.DecimalField(max_digits=5,decimal_places=2)
    fecha = models.DateTimeField()
     
    def __str__(self):
        return str(self.puntuacion)
    
    
