from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    user = models.ForeignKey('auth.User', null=True, blank=True, on_delete=models.CASCADE)
    telefoneComercial = models.CharField('Telefone Comercial', max_length=100)
    telefoneResidencial = models.CharField('Telefone Residencial', max_length=100)
    celular1 = models.CharField('Celular 1', max_length=100)
    celular2 = models.CharField('Celular 2',max_length=100)

    cep = models.CharField("CEP",  max_length=9)
    logradouro = models.CharField("Logradouro", max_length=150)
    numero = models.PositiveIntegerField('Número');
    complemento = models.CharField("Complemento", max_length=150)
    bairro = models.CharField("Bairro", max_length=30)
    cidade = models.CharField("Cidade", max_length=30)
    estado = models.CharField("Estado", max_length=2)

    def __str__(self):
        return self.nome