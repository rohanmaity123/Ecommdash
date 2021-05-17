from django import forms
from .models import category


class categoryform(forms.ModelForm):
    class Meta:
        model = category
        fields = ['name','image']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control',
            'id':'nameid',
            'placeholder':'Type your Category Name'
            }),
            'image':forms.TextInput(attrs={'class':'form-control',
            'type':'file',
            'id':'imageid'
            })
        }