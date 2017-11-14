from django import forms
from .models import Molho


class MolhoForm(forms.ModelForm):
    
    class Meta:
        model = Molho
        fields = [ 'descricao', ]