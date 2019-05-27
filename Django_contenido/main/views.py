from django.shortcuts import render
from main import forms,models

# Create your views here.

def artistasUsiario(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = forms.artistasMasEscuchados(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            id = form.cleaned_data['id']
            artistas = models.UsuarioArtista.objects.filter(usuario_id = id)
            print(artistas)
            return render(request, 'artistasUsiario.html', {'form': form,'artistas':artistas})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = forms.artistasMasEscuchados()
    return render(request, 'artistasUsiario.html', {'form': form})