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
from numpy import character
# Create your views here.

def inicio(request):
    characters = models.Character.objects.all()
    return render(request,'inicio.html',{'characters':characters})

# def crearPersonaje_nofunciona(request):
#     if request.method == 'POST':
#         form = forms.newCharacter(request.POST)
#         if form.is_valid():
#             print("b")
#             form.save()
#             return HttpResponseRedirect('../')
#     else:
#         form = forms.newCharacter()       
#     return render(request,'crearPersonaje.html',{'form':form})
# def load_subclass(request):
#     clas = request.GET.get('classCharacter')
#     subclasses = Subclass.objects.filter(fromClass_id=clas).order_by('name')
#     return render(request, 'hr/city_dropdown_list_subclass.html', {'subclasses': subclasses})

def newCharacter(request):
    if request.method == 'POST':
        form = forms.newCharacter(request.POST)
        if form.is_valid():         
            character = form.save()
            return HttpResponseRedirect("/seleccionarSubclase/"+ str(character.id))
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
#         spell = get_object_or_404(models.Subclass, pk= request.POST['spell'])
        print("---------------")
        spellList = list()
        for spell in request.POST.getlist('spellss'):
            spel = get_object_or_404(models.Spell, pk=spell )
            spellList.append(spel)
        character.spells.add(*spellList)
        character.save()
        return HttpResponseRedirect("../")
    character = get_object_or_404(models.Character, pk=character_id)
    charSubClass = character.subclass
    charMaxSpellLevel = character.level // 2
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
    return render(request,'personajeSeleccionado.html/' + str(character_id))

def modificarStats(request):
    return render(request,'modificarStats.html')

def searchSpell(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = searchSpellByName(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            spellName = form.cleaned_data['name']
            spells = Spell.objects.filter(name__icontains=spellName)
            return render(request, 'searchSpell.html', {'form': form,'spellName':spellName,'spells':spells})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = searchSpellByName()
    return render(request,'searchSpell.html',{'form': form})

def seleccionarHechizos(request):
    return render(request,'seleccionarHechizos.html')

def recomendarHechizos(request):
    recommendation(Character.objects.get(name='pruebaSpells'))
    return render(request,'recomendarHechizos.html')

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
#     def get_success_url(self, request, user):
#         return "/"