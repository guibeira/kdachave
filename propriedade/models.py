from django.db import models
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class Propriedade(models.Model):
    TIPO_PROPRIEDADE = (
                        (1, 'Apartamento'),
                        (2, 'Casa'),
                        (3, 'Comercio'),
                    )
    nome = models.CharField(max_length=50)
    pessoa = models.ForeignKey('pessoa.Pessoa')
    tipoPropriedade = models.IntegerField("Tipo Propriedade",
                                            choices=TIPO_PROPRIEDADE,
                                            default=1,
                                        )
    cep = models.CharField("CEP",  max_length=9)
    logradouro = models.CharField("Logradouro", max_length=150)
    numero = models.IntegerField()
    complemento = models.CharField("Complemento", max_length=150, null=True, blank=True)
    bairro = models.CharField("Bairro", max_length=30)
    cidade = models.CharField("Cidade", max_length=30)
    estado = models.CharField("Estado", max_length=2)

    def __str__(self):
        return self.nome