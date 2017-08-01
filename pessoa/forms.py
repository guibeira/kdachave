from django import forms
from .models import Pessoa


class ProprietarioForm(forms.ModelForm):

    class Meta:
        model = Pessoa
        fields = ['nome','telefoneComercial', 'telefoneResidencial', 'celular1', 'celular2', 'endereco', ]

class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ['user', 'nome','telefoneComercial', 'telefoneResidencial', 'celular1', 'celular2', 'endereco', ]
