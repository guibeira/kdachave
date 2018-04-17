from django import forms
from .models import Pessoa
from django.contrib.auth.models import User

class PessoaForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['telefoneComercial'].widget.attrs['class'] = 'fone'
    class Meta:
        model = Pessoa
        fields = [
                    'nome',
                    'user',
                    'telefoneComercial',
                    'telefoneResidencial',
                    'celular1',
                    'celular2',
                    'cep',
                    'logradouro',
                    'numero',
                    'complemento',
                    'bairro',
                    'cidade',
                    'estado',
                ]

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username', ]

class UserWithoutPasswordForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', ]
