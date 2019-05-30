from django.core.management.base import BaseCommand, CommandError
from main.scrapingSpells import lecturaSpells
from main.models import Spell,Class,Subclass
from django.contrib.auth.models import User

class Command(BaseCommand):
    
    help = 'Persistent dictionaries from DB'
    
    def handle(self, *args, **options):
        User.objects.create_superuser(username='admin', password='admin', email='admin@email.com')
        
        spells = lecturaSpells()
        for spell in spells:
            hechizo = Spell(name=spell["name"],level=spell["level"],school=spell["school"],
                                  castingTime=spell["castingTime"],hasRitual=spell["hasRitual"],
                                  requireConcentration=spell["requireConcentration"],
                                  range=spell["range"],components=spell["components"],
                                  duration=spell["duration"],description=spell["description"])
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