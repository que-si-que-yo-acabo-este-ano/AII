# Recomendar solo spells que no se tengan ya, se tengan disponibles por clase y nivel
# Priorizar spells del ultimo nivel disponible, y del anterior pero en menor medida.
# Penalizar spells que sean iguales en cuanto a duracion, tiempo de casteo y rango

from main.models import Spell, Class, Subclass, Character
from django.db.models import Q

def recommendation(character): # Sustituir todo por character y llamar a cada propiedad 
    charSubClass = character.subclass
    charMaxSpellLevel = character.level+1 // 2
    charClass = character.classCharacter
    charSpells = character.spells.all()
    charSpellsNames = character.spells.values_list('name',flat=True)
    
    if charSubClass:
        spells = Spell.objects.filter(Q(level__lte = charMaxSpellLevel), Q(classes__in = [Class.objects.get(name = charClass)]) | Q(subclasses__in = [Subclass.objects.get(name = charSubClass)])).distinct().exclude(name__in=charSpellsNames)
    else:
        spells = Spell.objects.filter(Q(level__lte = charMaxSpellLevel), Q(classes__in = [Class.objects.get(name = charClass)])).distinct().exclude(name__in=charSpellsNames)
    
    
    weightedSpells = []
    
    for spell in spells:
        total = len(charSpells)
        duration = spell.duration
        durationCount = 0
        castingTime = spell.castingTime
        castingTimeCount = 0
        distance = spell.range
        rangeCount = 0
        spellType = spell.type
        spellTypeCount = 0
        levelWeight = 0
        
        for known in charSpells:
            testDuration = duration != known.duration
            testCastingTime = castingTime != known.castingTime
            testDistance = distance != known.range
            testSpellType = spellType != known.type
            if testDuration:
                durationCount += 1
            if testCastingTime:
                castingTimeCount += 1
            if testDistance:
                rangeCount += 1
            if testSpellType:
                spellTypeCount += 1
        
        if spell.level == charMaxSpellLevel:
            levelWeight = 1
        elif (spell.level == charMaxSpellLevel-1):
            levelWeight = 0.85
        else:
            levelWeight = 0.5
            
        
        sim = (((durationCount/total)/3 + (castingTimeCount/total)/3 + (rangeCount/total)/3)*0.35 + (spellTypeCount/total)*0.5 + levelWeight*0.15)
        
        weightedSpells.append((spell,sim))
    
    
    weightedSpells.sort(key= lambda x: -x[1])
    print(weightedSpells)
    return weightedSpells[:5]
    
        
        
        
        