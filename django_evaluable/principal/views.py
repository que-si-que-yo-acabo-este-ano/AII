from django.shortcuts import render
from django.template.context_processors import request
from principal import forms
from django.http import HttpResponseRedirect
from principal import models

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

def noticiasPorDiario(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = forms.noticiaPorDiario(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            nombreDiario = form.cleaned_data['nombreDiario']
            noticias = models.Noticia.objects.filter(diario__nombre = nombreDiario)
            print(noticias)
            return render(request, 'noticiasPorDiario.html', {'form': form,'noticias':noticias})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = forms.noticiaPorDiario()
    return render(request, 'noticiasPorDiario.html', {'form': form})
    
    
    
    
    
    
    
    
    
    
