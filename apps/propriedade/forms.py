from django import forms
from .models import Propriedade


class PropriedadeForm(forms.ModelForm):
    
    class Meta:
        model = Propriedade
        fields = [ 
        			'nome', 
        			'tipoPropriedade', 
        			'pessoa', 
        			'cep',
					'logradouro',
					'numero',
					'complemento',
                    'bairro',
					'cidade',
					'estado',
        		]