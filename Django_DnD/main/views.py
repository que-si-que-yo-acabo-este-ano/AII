from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
# Create your views here.

def inicio(request):
    return render(request,'inicio.html')

def crearPersonaje(request):
    return render(request,'crearPersonaje.html')

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