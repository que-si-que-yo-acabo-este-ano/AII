from django.shortcuts import render
from main import forms
from main.models import Subclass,Class
from django.http import HttpResponseRedirect

# Create your views here.

def inicio(request):
    return render(request,'inicio.html')

def crearPersonaje(request):
    if request.method == 'POST':
        form = forms.newCharacter(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('../')
    else:
        form = forms.newCharacter()       
    return render(request,'crearPersonaje.html',{'form':form})

def load_subclass(request):
    clas = request.GET.get('classCharacter')
    print(clas)
    subclasses = Subclass.objects.filter(fromClass_id=clas).order_by('name')
    print(subclasses)
    return render(request, 'hr/city_dropdown_list_subclass.html', {'subclasses': subclasses})


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