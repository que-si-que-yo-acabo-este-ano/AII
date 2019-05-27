from django.db import models

# Create your models here.
class Usuario(models.Model):
    idUsuario = models.IntegerField(primary_key=True)
    
class Etiqueta(models.Model):
    idTag = models.IntegerField(primary_key=True)
    tagValue = models.CharField(max_length=20)
    
    def __str__(self):
        return self.tagValue
    
class Artista(models.Model):
    idArtista = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    url = models.URLField(null=True)
    pictureUrl = models.URLField(null=True)
    
    def __str__(self):
        return self.nombre
    
class UsuarioArtista(models.Model):
    usuario = models.ForeignKey("Usuario", on_delete=models.CASCADE)
    artista = models.ForeignKey("Artista", on_delete=models.CASCADE)
    tiempoEscucha = models.IntegerField()
    
    def __str__(self):
        return str(self.tiempoEscucha)
    
class UsuarioEtiquetaArtista(models.Model):
    usuario = models.ForeignKey("Usuario", on_delete=models.CASCADE)
    artista = models.ForeignKey("Artista", on_delete=models.CASCADE)
    etiqueta = models.ForeignKey("Etiqueta", on_delete=models.CASCADE) 
    dia = models.IntegerField()
    mes = models.IntegerField()
    anyo = models.IntegerField()
    