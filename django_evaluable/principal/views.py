from django.shortcuts import render
from django.template.context_processors import request
from principal import forms
from django.http import HttpResponseRedirect

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

def nuevaNoticia(request):
    if request.method == 'POST':
        form = forms.nuevaNoticia(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('../')
    else:
        form = forms.nuevaNoticia()
        
    return render(request,'nuevaNoticia.html',{'form':form})

def nuevoTipoNoticia(request):
    if request.method == 'POST':
        form = forms.nuevoTipoNoticia(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('../')
    else:
        form = forms.nuevoTipoNoticia()
        
    return render(request,'nuevoTipoNoticia.html',{'form':form})
