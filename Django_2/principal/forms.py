from django import forms
from principal import models   
from dataclasses import fields

class PeliculaForm(forms.ModelForm):
    class Meta:
        model = models.Pelicula
        fields = ['peliculaID','titulo','imdbID','tmdbID']
        
        