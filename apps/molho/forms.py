from django import forms
from .models import Molho


class MolhoForm(forms.ModelForm):

    class Meta:
        model = Molho
        fields = ['descricao', 'chaves', 'controles', 'observacao']


class MolhoBulkEdition(forms.ModelForm):
    class Meta:
        model = Molho
        fields = ['observacao']
        widgets = {'observacao': forms.Textarea(attrs={'rows':1, 'cols':15}),}
