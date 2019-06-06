from django import forms
from .models import Character,Subclass   
from itertools import chain
from dataclasses import fields


# lo que no funciona
# class newCharacter(forms.ModelForm):
#     class Meta:
#         model = Character
#         fields = ['name','classCharacter','race','subclass','level','strength','dexterity','constitution',
#                   'intelligence','wisdom','charisma','maxHP','armorClass','spells']
#          
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['subclass'].queryset = Subclass.objects.none()
#         print("a")
#         if 'classCharacter' in self.data:
#             print("b")
#             try:
#                 classCharacter_name = self.data.get('classCharacter')
#                 subclases =  Subclass.objects.all()
#                 my_obj_list = []
#                 for subclass_item in subclases:
#                     print(subclass_item.fromClass.name)
#                     print(classCharacter_name)
#                     print("-----------------------------")
#                     if subclass_item.fromClass.name == classCharacter_name:
#                         print("ji")
#                         my_obj_list.append(subclass_item)
#                 #self.fields['subclass'].queryset = Subclass.objects.filter(fromClass_name=classCharacter).order_by('name')
#                 print(my_obj_list)
#                 #and then 
#                 none_qs = Subclass.objects.none()
#                 print("casi casi")
#                 self.fields['subclass'].queryset = Subclass.objects.get(my_obj_list)
#                 print(self.fields['subclass'].queryset)
#                 
#             except (ValueError, TypeError):
#                 print("mierda")
#                 pass  # invalid input 
#         elif self.instance.pk:
#             print("c")
#             self.fields['subclass'].queryset = self.instance.classCharacter.subclass_set.order_by('name')
#         print("d")

class newCharacter(forms.ModelForm):
    class Meta:
        model = Character
        fields = ['name','classCharacter','race','level','strength','dexterity','constitution',
                  'intelligence','wisdom','charisma','maxHP','armorClass']
        
class selectSubclass(forms.ModelForm):
    class Meta:
        model = Character
        fields =["subclass"]
        
class selectSpells(forms.ModelForm):
    class Meta:
        model = Character
        fields =["spells"]
    

        
