from django.db import models
from apps.core.models import Endereco


class Propriedade(Endereco):
    TIPO_PROPRIEDADE = (
                        (1, 'Apartamento'),
                        (2, 'Casa'),
                        (3, 'Comercio'),
                    )
    nome = models.CharField(max_length=50)
    pessoa = models.ForeignKey('pessoa.Pessoa')
    tipoPropriedade = models.IntegerField(
                                            "Tipo Propriedade",
                                            choices=TIPO_PROPRIEDADE,
                                            default=1,
                                        )

    def __str__(self):
        return self.nome
