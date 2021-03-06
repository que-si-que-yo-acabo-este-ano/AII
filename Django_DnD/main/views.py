from django.shortcuts import render
from main import forms
from main.models import Subclass, Class, Character, Spell
from main.cbrs import recommendation
from django.http import HttpResponseRedirect
from .forms import searchSpellByName
from main import models
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.template.context_processors import request
# Create your views here.

def inicio(request):
    characters = models.Character.objects.all()
    return render(request,'inicio.html',{'characters':characters})

def newCharacter(request):
    if request.method == 'POST':
        form = forms.newCharacter(request.POST)
        if form.is_valid():         
            character = form.save(commit=False)
            character.user = request.user
            character.save()
            subclasses = list(Subclass.objects.values_list("fromClass").distinct())
            subclassesAvailables = [subclase[0] for subclase in subclasses]
            if character.classCharacter.name in subclassesAvailables:
                return HttpResponseRedirect("/seleccionarSubclase/"+ str(character.id))
            else:
                return HttpResponseRedirect("/seleccionarHechizos/"+ str(character.id))
    else:
        form = forms.newCharacter()
        
    return render(request,'crearPersonaje.html',{'form':form})

def selectSubclass(request,character_id):
    if request.method == 'POST':
        character = get_object_or_404(models.Character, pk=character_id)
        subclass = get_object_or_404(models.Subclass, pk= request.POST['subclass'])
        character.subclass = subclass
        character.save()
        return HttpResponseRedirect('/seleccionarHechizos/' + str(character.id))
    character = get_object_or_404(models.Character, pk=character_id)
    subclasses = Subclass.objects.filter(fromClass__name = character.classCharacter)
    return render(request,'seleccionarSubclase.html',{'subclasses':subclasses,'character':character})

def selecSpells(request,character_id):
    if request.method == 'POST':
        character = get_object_or_404(models.Character, pk=character_id)
        spellList = list()
        for spell in request.POST.getlist('spellss'):
            spel = get_object_or_404(models.Spell, pk=spell )
            spellList.append(spel)
        character.spells.add(*spellList)
        character.save()
        return HttpResponseRedirect("../")
    character = get_object_or_404(models.Character, pk=character_id)
    charSubClass = character.subclass
    charMaxSpellLevel = (character.level+1) // 2
    charClass = character.classCharacter
    charSpellsNames = character.spells.values_list('name',flat=True)
    if charSubClass:
        spells = Spell.objects.filter(Q(level__lte = charMaxSpellLevel), Q(classes__in = [Class.objects.get(name = charClass)]) | Q(subclasses__in = [Subclass.objects.get(name = charSubClass)])).distinct()
    else:
        spells = Spell.objects.filter(Q(level__lte = charMaxSpellLevel), Q(classes__in = [Class.objects.get(name = charClass)])).distinct()
    
    return render(request,'seleccionarHechizos.html',{'spells':spells,'character':character})
    
def mostrarHechizos(request):
    spells = Spell.objects.all()
    return render(request,'mostrarHechizos.html', {'spells':spells})

def personajeSeleccionado(request,character_id):
    character = get_object_or_404(models.Character, pk=character_id)
    return render(request,'personajeSeleccionado.html/',{'character':character})

def modificarStats(request,character_id):
    if request.method == 'POST':
        form = forms.modifyStats(request.POST)
        if form.is_valid():
            character = get_object_or_404(models.Character, pk=character_id)
            if form.cleaned_data['lvl'] != None : character.level = form.cleaned_data['lvl']
            if form.cleaned_data['str'] != None : character.strength = form.cleaned_data['str']
            if form.cleaned_data['dxt'] != None : character.dexterity = form.cleaned_data['dxt']
            if form.cleaned_data['const'] != None : character.constitution = form.cleaned_data['const']
            if form.cleaned_data['int'] != None : character.intelligence = form.cleaned_data['int']
            if form.cleaned_data['wsd'] != None : character.wisdom = form.cleaned_data['wsd']
            if form.cleaned_data['cha'] != None : character.charisma = form.cleaned_data['cha']
            character.save()
            return HttpResponseRedirect('../personajeSeleccionado/' + str(character_id))
    else:
        form = forms.modifyStats()
    character = get_object_or_404(models.Character, pk=character_id)
    return render(request,'modificarStats.html',{'form':form ,'character':character})

def searchSpell(request):
    if request.method == 'POST':
        form = searchSpellByName(request.POST)
        if form.is_valid():
            spellName = form.cleaned_data['name']
            spells = Spell.objects.filter(name__icontains=spellName)
            return render(request, 'searchSpell.html', {'form': form,'spellName':spellName,'spells':spells})
    else:
        form = searchSpellByName()
    return render(request,'searchSpell.html',{'form': form})

def seleccionarNuevosHechizos(request,character_id):
    if request.method == 'POST':
        character = get_object_or_404(models.Character, pk=character_id)
        spellList = list()
        for spell in request.POST.getlist('spellss'):
            spel = get_object_or_404(models.Spell, pk=spell )
            spellList.append(spel)
        character.spells.add(*spellList)
        character.save()
        return HttpResponseRedirect("../personajeSeleccionado/" + str(character_id))
    character = get_object_or_404(models.Character, pk=character_id)
    charSubClass = character.subclass
    charMaxSpellLevel = (character.level+1) // 2
    charClass = character.classCharacter
    charSpellsNames = character.spells.values_list('name',flat=True)
    if charSubClass:
        spells = Spell.objects.filter(Q(level__lte = charMaxSpellLevel), Q(classes__in = [Class.objects.get(name = charClass)]) | Q(subclasses__in = [Subclass.objects.get(name = charSubClass)])).distinct()
    else:
        spells = Spell.objects.filter(Q(level__lte = charMaxSpellLevel), Q(classes__in = [Class.objects.get(name = charClass)])).distinct()
    spellsNoSelected = []
    for spell in spells:
        if not spell in character.spells.all(): spellsNoSelected.append(spell)
        
    return render(request,'seleccionarNuevosHechizos.html',{'spells':spellsNoSelected,'character':character})

def deseleccionarHechizos(request,character_id):
    if request.method == 'POST':
        character = get_object_or_404(models.Character,pk=character_id)
        spellList = list()
        for spell in request.POST.getlist('spells'):
            hechizo = get_object_or_404(models.Spell,pk=spell)
            spellList.append(hechizo)
        character.spells.remove(*spellList)
        character.save()
        return HttpResponseRedirect("../personajeSeleccionado/" + str(character_id))
    character = get_object_or_404(models.Character,pk=character_id)
    spells = character.spells.all()
    return render(request,'deseleccionarHechizos.html',{'spells':spells,'character':character})


def recomendarHechizos(request,character_id):
    character = get_object_or_404(models.Character,pk=character_id)
    spells = []
    if character.spells.exists():
        spells = recommendation(character)
    return render(request,'recomendarHechizos.html',{'spells': spells,'characterName':character.name,'character':character})

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
#     def get_success_url(self, request, user):
#         return "/"