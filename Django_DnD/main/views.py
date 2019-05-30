from django.shortcuts import render

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