from django.contrib import admin
from main.models import Character,Class, Subclass, Race, Spell

# Register your models here.
admin.site.register(Character)
admin.site.register(Class)
admin.site.register(Subclass)
admin.site.register(Race)
admin.site.register(Spell)