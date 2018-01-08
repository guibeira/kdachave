from django.db import models
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class Propriedade(models.Model):

    nome = models.CharField(max_length=50)
    numero = models.IntegerField()
    tipo = models.ForeignKey('TipoPropriedade')
    endereco = models.ForeignKey('endereco.Endereco', null=True)
    complemento = models.CharField(max_length=100)
    pessoa = models.ForeignKey('pessoa.Pessoa')

    def __str__(self):
        return self.nome
    

class TipoPropriedade(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


