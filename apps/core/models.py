from django.db import models
from localflavor.br.br_states import STATE_CHOICES


class Endereco(models.Model):
    cep = models.CharField("CEP",  max_length=9)
    logradouro = models.CharField("Logradouro", max_length=150)
    numero = models.IntegerField()
    complemento = models.CharField(
                                    "Complemento", max_length=150, null=True,
                                    blank=True
                                    )
    bairro = models.CharField("Bairro", max_length=30)
    cidade = models.CharField("Cidade", max_length=30)
    estado = models.CharField(max_length=2, choices=STATE_CHOICES)

    class Meta:
        abstract = True
