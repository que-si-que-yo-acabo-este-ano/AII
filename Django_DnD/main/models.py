from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.fields.related import ManyToManyField
from django.contrib.auth.models import User

# Create your models here.
class Class(models.Model):
    name = models.CharField(primary_key=True,max_length=20)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Classes"
    

class Subclass(models.Model):
    name = models.CharField(primary_key=True,max_length=20)
    fromClass = models.ForeignKey("Class",on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Subclasses"
    

class Character(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=15)
    race = models.ForeignKey("Race",on_delete=models.CASCADE)
    classCharacter = models.ForeignKey("Class",on_delete=models.CASCADE)
    subclass = models.ForeignKey("Subclass",on_delete=models.CASCADE)
    level = models.IntegerField(validators=[MinValueValidator(0)])
    strength = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)])
    dexterity = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)])
    constitution = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)])
    intelligence = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)])
    wisdom = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)])
    charisma = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)])
    maxHP = models.IntegerField(validators=[MinValueValidator(0)])
    armorClass = models.IntegerField(validators=[MinValueValidator(0)])
    spells = ManyToManyField("Spell")
    
    def __str__(self):
        return self.name

class Race(models.Model):
    name = models.CharField(primary_key=True, max_length=20)
    
    def __str__(self):
        return self.name
    
class Spell(models.Model):
    name = models.CharField(primary_key=True,max_length=20)
    level = models.IntegerField(validators=[MinValueValidator(0)])
    school = models.CharField(max_length=20)
    castingTime = models.CharField(max_length=20)
    components = models.CharField(max_length=40)
    duration = models.CharField(max_length=20)
    range = models.CharField(max_length=30)
    hasRitual = models.BooleanField()
    requireConcentration = models.BooleanField()
    classes = models.ManyToManyField("Class")
    subclasses = models.ManyToManyField("Subclass")
    description = models.TextField()
    
    def __str__(self):
        return self.name

