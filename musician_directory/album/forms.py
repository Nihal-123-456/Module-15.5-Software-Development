from django import forms
from .models import *

class AlbumForm(forms.ModelForm):
    
    class Meta:
        model = Album
        fields = '__all__'
        rating_choice = [('1','1'),('2','2'),('3','3'),('4','4'),('5','5')]
        widgets = {
            'rating': forms.RadioSelect(choices=rating_choice),
            'release_date' : forms.NumberInput(attrs={'type': 'date'})
        }