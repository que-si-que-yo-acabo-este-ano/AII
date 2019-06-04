# Recomendar solo spells que no se tengan ya, se tengan disponibles por clase y nivel
# Priorizar spells del ultimo nivel disponible, y del anterior pero en menor medida.
# Penalizar spells que sean iguales en cuanto a duracion, tiempo de casteo y rango

from main.models import Spell, Class, Subclass, Character
from django.db.models import Q

def recommendation(character): # Sustituir todo por character y llamar a cada propiedad 
    charSubClass = character.subclass
    charLevel = character.level
    charClass = character.classCharacter
    charSpellsNames = character.spells.values_list('name',flat=True)
    
    if charSubClass:
        spells = Spell.objects.filter(Q(level__lte = charLevel), Q(classes__in = [Class.objects.get(name = charClass)]) | Q(subclasses__in = [Subclass.objects.get(name = charSubClass)])).distinct().exclude(name__in=charSpellsNames)
    else:
        spells = Spell.objects.filter(Q(level__lte = charLevel), Q(classes__in = [Class.objects.get(name = charClass)])).distinct().exclude(name__in=charSpellsNames)
    
    
    
    
    
    setPrueba = set([])
    
    
    for spell in spells:
        setPrueba.add(spell.duration)
        
    
    for one in setPrueba:
        print(one)