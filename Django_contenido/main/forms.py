from django import forms
from main import models

class artistasMasEscuchados(forms.Form):
    id = forms.IntegerField()