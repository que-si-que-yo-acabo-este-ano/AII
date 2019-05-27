from django.shortcuts import render
from main import forms,models

# Create your views here.

def artistasUsuario(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = forms.artistasMasEscuchados(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            id = form.cleaned_data['id']
            artistasUsuarios = models.UsuarioArtista.objects.filter(usuario__idUsuario = id)
            print(artistasUsuarios)
            return render(request, 'artistasUsuario.html', {'form': form,'artistasUsuarios':artistasUsuarios,'id':id})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = forms.artistasMasEscuchados()
    return render(request, 'artistasUsuario.html', {'form': form})