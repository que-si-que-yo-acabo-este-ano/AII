from django import forms
from .models import Character,Subclass   
from itertools import chain
from dataclasses import fields
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

class newCharacter(forms.ModelForm):
    class Meta:
        model = Character
        fields = ['name','classCharacter','race','level','strength','dexterity','constitution',
                  'intelligence','wisdom','charisma','maxHP','armorClass']
        
class selectSubclass(forms.Form):
    subclassSselected = forms.CharField(max_length=50)
        
class modifyStats(forms.Form):
    lvl = forms.IntegerField(required = False,validators=[MinValueValidator(0)])
    str = forms.IntegerField(required = False,validators=[MinValueValidator(0), MaxValueValidator(20)])
    dxt = forms.IntegerField(required = False,validators=[MinValueValidator(0), MaxValueValidator(20)])
    const = forms.IntegerField(required = False,validators=[MinValueValidator(0), MaxValueValidator(20)])
    int = forms.IntegerField(required = False,validators=[MinValueValidator(0), MaxValueValidator(20)])
    wsd = forms.IntegerField(required = False,validators=[MinValueValidator(0), MaxValueValidator(20)])
    cha = forms.IntegerField(required = False,validators=[MinValueValidator(0), MaxValueValidator(20)])
    
class searchSpellByName(forms.Form):
    name = forms.CharField(max_length=20)
    
class recommendSpell(forms.Form):
    name = forms.CharField(max_length=20)