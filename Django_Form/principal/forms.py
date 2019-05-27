import datetime
from django import forms
from django.core.exceptions import ValidationError


class FilmsOfYearForm(forms.Form):
    year = forms.IntegerField(max_value=2020, min_value=1900, help_text="Enter a year to display films from")

class UserInputForm(forms.Form):
    user = forms.CharField(help_text='User')