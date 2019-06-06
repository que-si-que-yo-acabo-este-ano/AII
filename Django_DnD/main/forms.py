from django import forms
from .models import Character,Subclass   

class newCharacter(forms.ModelForm):
    class Meta:
        model = Character
        fields = ['name','classCharacter','race','subclass','level','strength','dexterity','constitution',
                  'intelligence','wisdom','charisma','maxHP','armorClass','spells']
         
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['subclass'].queryset = Subclass.objects.none()
    
class searchSpellByName(forms.Form):
    name = forms.CharField(max_length=20)