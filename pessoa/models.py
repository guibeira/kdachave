from django.db import models
from core.models import Endereco


class Pessoa(Endereco):
    nome = models.CharField(max_length=100)
    user = models.ForeignKey(
                                'auth.User',
                                null=True,
                                blank=True,
                                on_delete=models.CASCADE)
    telefoneComercial = models.CharField(
                                        'Telefone Comercial',
                                        max_length=100,
                                        null=True,
                                        blank=True)
    telefoneResidencial = models.CharField(
                                            'Telefone Residencial',
                                            max_length=100,
                                            null=True,
                                            blank=True)
    celular1 = models.CharField(
                                'Celular 1',
                                max_length=100,
                                null=True,
                                blank=True)
    celular2 = models.CharField(
                                'Celular 2',
                                max_length=100,
                                null=True,
                                blank=True)

    def __str__(self):
        return self.nome
