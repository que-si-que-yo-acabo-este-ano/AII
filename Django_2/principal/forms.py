from django import forms
from principal import models   
from dataclasses import fields


class PeliculaForm(forms.ModelForm):
    generosElegir = forms.ModelMultipleChoiceField(models.Genero.objects.all(), required=False)
    
    class Meta:
        model = models.Pelicula
        fields = ['peliculaID','titulo','imdbID','tmdbID']
        
        
import datetime
from django import forms
from django.core.exceptions import ValidationError


class FilmsOfYearForm(forms.Form):
    year = forms.IntegerField(max_value=2020, min_value=1900, help_text="Enter a year to display films from")
    title = forms.CharField()