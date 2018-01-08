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
    endereco = models.ForeignKey('endereco.Endereco')
    numeroEndereco = models.PositiveIntegerField('Numero do Endereço');

    def __str__(self):
        return self.nome
