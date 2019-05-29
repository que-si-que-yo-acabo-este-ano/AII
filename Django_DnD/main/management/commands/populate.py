from django.core.management.base import BaseCommand, CommandError
from main.scrapingSpells import lecturaSpells


class Command(BaseCommand):
    
    help = 'Persistent dictionaries from DB'
    
    def handle(self, *args, **options):
        spells = lecturaSpells()