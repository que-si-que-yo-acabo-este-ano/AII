from django.conf import settings
# from principal.models import Usuario,Pelicula,Puntuacion,Categoria,CategoriaPelicula,Ocupacion,Puntuacion
import os
from django.core.management.base import BaseCommand, CommandError
from datetime import datetime
from django_evaluable.settings import STATIC_ROOT
from django.contrib.auth.models import User

class Command(BaseCommand):
    
    help = 'Populate from u.* to database'
    
    def handle(self, *args, **options):
        pass