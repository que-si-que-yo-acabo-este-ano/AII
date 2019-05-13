from django import forms
from principal import models   
from dataclasses import fields


class PeliculaForm(forms.ModelForm):
    generosElegir = forms.ModelMultipleChoiceField(models.Genero.objects.all(), required=False)
    
    class Meta:
        model = models.Pelicula
        exclude = ['generos']
        fields = ['peliculaID','titulo','imdbID','tmdbID']  
    