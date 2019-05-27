from django import forms
from main import models

class artistasMasEscuchados(forms.Form):
    id = forms.IntegerField()
    
class artistTopTags(forms.Form):
    id = forms.IntegerField()