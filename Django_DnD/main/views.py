from django.shortcuts import render
from main import forms
from main.models import Subclass,Class
from django.http import HttpResponseRedirect
from main import models
from django.shortcuts import get_object_or_404

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.template.context_processors import request
from numpy import character
# Create your views here.

def inicio(request):
    return render(request,'inicio.html')

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
#             nameClass = form.cleaned_data['classCharacter']
#             subclasses = Subclass.objects.filter(fromClass__name = nameClass)
            
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

# def selecSpells(request,character_id):
#     if request.method == 'POST'
#         print("meh")
#     
#     character = get_object_or_404(models.Character, pk=character_id)
#     spells = models.Spell.objects.filter(subclasses == character.subclass)
    
    
    
def mostrarHechizos(request):
    return render(request,'mostrarHechizos.html')

def personajeSeleccionado(request):
    return render(request,'personajeSeleccionado.html')

def modificarStats(request):
    return render(request,'modificarStats.html')

def seleccionarHechizos(request):
    return render(request,'seleccionarHechizos.html')

def recomendarHechizos(request):
    return render(request,'recomendarHechizos.html')

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
#     def get_success_url(self, request, user):
#         return "/"