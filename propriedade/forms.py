from django import forms
from .models import Propriedade


class PropriedadeForm(forms.ModelForm):
    
    class Meta:
        model = Propriedade
        fields = ['tipo', 'proprietario' , 'complemento', 'numero']