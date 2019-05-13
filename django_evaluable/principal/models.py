from django.db import models

# Create your models here.
class Diario(models.Model):
    nombre = models.CharField(max_length=100,primary_key=True)
    pais = models.CharField(max_length=20)
    idioma = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    nombreUsuario = models.CharField(max_length=20,primary_key=True)
    passwd = models.CharField(max_length=10)
    email = models.EmailField()
    nombre = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nombreUsuario
    
class Autor(models.Model):
    nombre = models.CharField(max_length=20,primary_key=True)
    apellidos = models.CharField(max_length=20) 
    email = models.EmailField()
    
    def __str__(self):
        return self.nombre
    
class Noticia(models.Model):
    titular = models.CharField(max_length=100,primary_key=True)
    fechaNoticia = models.DateField()
    resumen = models.TextField()
    tipos = (('Deportes','Deportes'),('Cultura','Cultura'),('Politica','Politica'),('Economia','Economia'),('Actualidad','Actualidad'))
    tipoNoticia = models.CharField(max_length=15,choices=tipos)
    diario = models.ForeignKey("Diario",on_delete=models.CASCADE)
    autores = models.ManyToManyField("Autor")
    usuarios = models.ManyToManyField("Usuario")
    
    
    