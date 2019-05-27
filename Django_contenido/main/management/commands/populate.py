from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from main.readData import readFile

class Command(BaseCommand):
    
    help = 'Populate from .dat to database'
    
    def handle(self, *args, **options):
        User.objects.create_superuser(username='admin', password='admin', email='admin@email.com')
