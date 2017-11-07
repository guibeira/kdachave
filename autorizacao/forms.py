from django import forms
from .models import Autorizacao


class AutorizacaoForm(forms.ModelForm):

    class Meta:
        model = Autorizacao
        fields = [  'descricao',
                    'dataInicio',
                    'dataFim',
                    'autorizada',
                    'criador',
                    'propriedade',
                    'status', ]
