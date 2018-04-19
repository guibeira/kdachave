from django import forms
from apps.registro.models import Registro
from apps.molho.models import Molho


class RegistroForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        registro = kwargs.pop('instance')
        if registro:
            propriedade = registro.propriedade
            choices = [(molho.pk, molho) for molho in Molho.objects.filter(propriedade=propriedade)]
            self.fields['molhos'].choices = choices
            self.fields['molhos'].initial = registro.molhos.all()

    class Meta:
        model = Registro
        fields = ['dataEntrega',
                  'dataPrevisaoRetorno',
                  'responsavel',
                  'propriedade',
                  'molhos'
                  ]


class RegistroSaidaGetForm(forms.ModelForm):

    class Meta:
        model = Registro
        fields = [
          'responsavel',
          'dataEntrega',
          'dataPrevisaoRetorno',
          'propriedade',
          ]


class RegistroSaidaPostForm(forms.ModelForm):

    class Meta:
        model = Registro
        fields = [
          'responsavel',
          'dataEntrega',
          'dataPrevisaoRetorno',
          'propriedade',
          'molhos',
          ]


class RegistroDevolucaoForm(forms.ModelForm):

    class Meta:
        model = Registro
        fields = ['molhos', 'dataRetorno']
