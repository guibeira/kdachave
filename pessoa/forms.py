from django import forms
from .models import Pessoa
from django.contrib.auth.models import User


class ProprietarioForm(forms.ModelForm):

    class Meta:
        model = Pessoa
        fields = ['nome','telefoneComercial', 'telefoneResidencial', 'celular1', 'celular2', 'endereco', 'numeroEndereco', ]

class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ['nome','telefoneComercial', 'telefoneResidencial', 'celular1', 'celular2', 'endereco', 'numeroEndereco', ]

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username', ]

class UserWithoutPasswordForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', ]
