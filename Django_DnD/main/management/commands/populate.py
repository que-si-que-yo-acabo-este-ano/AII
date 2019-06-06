from django.core.management.base import BaseCommand, CommandError
from main.scrapingSpells import lecturaSpells
from main.models import Spell,Class,Subclass,Race
from django.contrib.auth.models import User
import re

class Command(BaseCommand):
    
    help = 'Persistent dictionaries from DB'
    
    def handle(self, *args, **options):
        User.objects.create_superuser(username='admin', password='admin', email='admin@email.com')
        regex_damage = re.compile(r'\d{1,2}[d]\d{1,2}\s\w+\sdamage')
        regex_healing = re.compile(r'(regains?((\s\d{1,2}[d]\d{1,2})|(\s\d+\s)).+hit\spoints)|(regains?.+hit\spoints.+((\s\d{1,2}[d]\d{1,2})|(\s\d+\s)))')
        spells = lecturaSpells()
        for spell in spells:
            tipo = ""
            descripcion = spell["description"]
            if regex_healing.search(descripcion):
                tipo = 'Healing'
            elif regex_damage.search(descripcion):
                tipo = 'Damage'
            else:
                tipo = 'Utility'
            hechizo = Spell(name=spell["name"],level=spell["level"],school=spell["school"],
                                  castingTime=spell["castingTime"],hasRitual=spell["hasRitual"],
                                  type = tipo,requireConcentration=spell["requireConcentration"],
                                  range=spell["range"],components=spell["components"],
                                  duration=spell["duration"],description=descripcion)
            hechizo.save()
            for classCharacter in spell["class"]:
                clase, isCreated = Class.objects.get_or_create(name=classCharacter)
                if isCreated:
                    clase.save()
                hechizo.classes.add(clase)
            for subclassCharacterKey in spell["subclass"].keys():
                clase, isCreated = Class.objects.get_or_create(name=subclassCharacterKey)
                if isCreated:
                    clase.save()
                for subclase in spell["subclass"][subclassCharacterKey]:
                    subclass,isCreated = Subclass.objects.get_or_create(name=subclase,
                                                                    fromClass = clase)
                    if isCreated:
                        subclass.save()
                    hechizo.subclasses.add(subclass)
         
        races = ["Dwarf","Elf","Hafling","Human","Dragonborn","Gnome","Half-Elf","Half-Orc","Tiefling"]
        razas = [Race(name=race) for race in races]
        Race.objects.bulk_create(razas)