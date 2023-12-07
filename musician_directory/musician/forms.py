from django import forms
from .models import *

class MusicianForm(forms.ModelForm):
    class Meta:
        model = Musician
        fields = '__all__'