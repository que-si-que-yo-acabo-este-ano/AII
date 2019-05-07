#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User
from unittest.util import _MAX_LENGTH
# Create your models here.
class Bebida(models.Model):
    nombre = models.CharField(max_length=50)
    ingredientes = models.TextField()
    preparacion = models.TextField()

    def __str__(self):
        return self.nombre
    
class Receta(models.Model):
    titulo = models.CharField(max_length=100, unique=True)
    ingredientes = models.TextField(help_text='Redacta los ingredientes')
    prepacion = models.TextField(verbose_name='Preparación')
    imagen = models.ImageField(upload_to='recetas', verbose_name='Imágen')
    tiempo_registro = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)
  
    def __str__(self):
        return self.titulo
 
   
class Usuario(models.Model):
    usuarioID = models.IntegerField(primary_key=True)

class Genero(models.Model):
    genero = models.TextField(primary_key=True)
    
# 
class Pelicula(models.Model):
    peliculaID = models.IntegerField(primary_key = True)
    titulo = models.CharField(max_length=100)    
    imbdID = models.IntegerField()
    thdbID = models.IntegerField()
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
        return self.puntuacion
    
    
