from django.shortcuts import render
from django.template.context_processors import request
from principal import forms
from django.http import HttpResponseRedirect

def inicio(request):
    return render(request,'inicio.html')

def formularios(request):
    return render(request,'formularios.html')

def nuevoDiario(request):
    if request.method == 'POST':
        form = forms.nuevoDiario(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('../')
    else:
        form = forms.nuevoDiario()
        
    return render(request,'nuevoDiario.html',{'form':form})

def nuevoUsuario(request):
    if request.method == 'POST':
        form = forms.nuevoUsuario(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('../')
    else:
        form = forms.nuevoUsuario()
        
    return render(request,'nuevoUsuario.html',{'form':form})

def nuevoAutor(request):
    if request.method == 'POST':
        form = forms.nuevoAutor(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('../')
    else:
        form = forms.nuevoAutor()
        
    return render(request,'nuevoAutor.html',{'form':form})