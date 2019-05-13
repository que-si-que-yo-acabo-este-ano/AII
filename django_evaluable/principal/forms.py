from django import forms
from principal import models
from django.contrib.contenttypes import fields

class nuevoDiario(forms.ModelForm):
    class Meta:
        model = models.Diario
        fields = ['nombre','pais','idioma']

class nuevoUsuario(forms.ModelForm):
    class Meta:
        model = models.Usuario
        fields = ['nombreUsuario','passwd','email','nombre','apellidos']

class nuevoAutor(forms.ModelForm):
    class Meta:
        model = models.Autor
        fields = ['nombre','apellidos','email']

