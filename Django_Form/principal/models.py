from django.db import models


class Usuario(models.Model):
    idUsuario = models.IntegerField(primary_key=True)
    edad = models.IntegerField()
    sexos = (('M','M'),('F','F'))
    sexo = models.CharField(max_length=1,choices=sexos)
    ocupacion = models.ForeignKey("Ocupacion",on_delete=models.CASCADE)
    codigoPostal = models.CharField(max_length=10)
    
    def __str__(self):
        return str(self.idUsuario)

class Pelicula(models.Model):
    idPelicula = models.IntegerField(primary_key=True)
    titulo = models.CharField(max_length=100)
    fechaDeEstreno = models.DateTimeField()
    imdbURL = models.URLField()
    categorias = models.ManyToManyField(
        "Categoria",
        through="CategoriaPelicula")
    puntuaciones = models.ManyToManyField(
        "Usuario",
        through="Puntuacion")
    
    def __str__(self):
        return self.titulo
    
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre
    
class CategoriaPelicula(models.Model):
    idCategoria = models.ForeignKey("Categoria",on_delete=models.CASCADE)
    idPelicula = models.ForeignKey("Pelicula",on_delete=models.CASCADE)    
    
class Ocupacion(models.Model):
    nombre = models.CharField(max_length = 100, primary_key=True)
    
    def __str__(self):
        return self.nombre

class Puntuacion(models.Model):
    idUsuario = models.ForeignKey("Usuario",on_delete=models.CASCADE)
    idPelicula = models.ForeignKey("Pelicula",on_delete=models.CASCADE)
    puntuacion = models.IntegerField()
    fecha = models.DateTimeField()
    def __str__(self):
        return str(self.puntuacion)
