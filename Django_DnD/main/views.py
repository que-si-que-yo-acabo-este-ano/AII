from django.shortcuts import render
from main import forms
from main.models import Subclass,Class
from django.http import HttpResponseRedirect

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.template.context_processors import request
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
            form.save()
            
            return HttpResponseRedirect('../')
    else:
        form = forms.newCharacter()
        
    return render(request,'crearPersonaje.html',{'form':form})



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