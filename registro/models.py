from django.db import models
from molho.models import Molho

class Registro(models.Model):
	dataEntrega = models.DateTimeField("Data Entrega")
	dataPrevisaoRetorno = models.DateTimeField("Data de Previsão do Retorno")
	dataRetorno = models.DateTimeField("Data Retorno")
	pessoaEntregue = models.ForeignKey('pessoa.Pessoa', related_name='pessoaEntregue')
	pessoaRecebeu = models.ForeignKey('pessoa.Pessoa', related_name='pessoaRecebeu')
	propriedade = models.ForeignKey('propriedade.Propriedade')
	molhos = models.ManyToManyField('molho.Molho')
	
	def __str__(self):
		return str(self.pessoaEntregue.nome)