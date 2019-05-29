from django.core.management.base import BaseCommand, CommandError
from main.scrapingSpells import lecturaSpells
from main.models import Spell

class Command(BaseCommand):
    
    help = 'Persistent dictionaries from DB'
    
    def handle(self, *args, **options):
        spells = lecturaSpells()
        ##TODO: Create classes, subclasses, race
        hechizos = []
        for spell in spells:
            hechizos.append(Spell(name=spell["name"]))
        