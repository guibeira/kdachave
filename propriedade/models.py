from django.db import models
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class Propriedade(models.Model):
    TIPO_PROPRIEDADE = (
                        (0, ''),
                        (1, 'Apartamento'),
                        (2, 'Casa'),
                        (3, 'Comercio'),
                    )
    nome = models.CharField(max_length=50)
    numero = models.IntegerField()
    endereco = models.ForeignKey('endereco.Endereco', null=True)
    pessoa = models.ForeignKey('pessoa.Pessoa')
    tipoPropriedade = models.IntegerField("Tipo Propriedade",
                                        choices=TIPO_PROPRIEDADE,
                                        default=0,
                                    )

    def __str__(self):
        return self.nome