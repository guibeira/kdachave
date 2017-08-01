from django.db import models


class Propriedade(models.Model):

    numero = models.IntegerField()
    tipo = models.ForeignKey('TipoPropriedade')
    endereco = models.ForeignKey('endereco.Endereco')
    proprietario = models.ForeignKey('pessoa.Pessoa')

    def __str__(self):
        return '{} {}'.format(self.proprietario, self.numero)
    

class TipoPropriedade(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
