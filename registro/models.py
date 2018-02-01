from django.db import models
from django.contrib.auth.models import User
from molho.models import Molho

class Registro(models.Model):
	dataEntrega = models.DateTimeField("Data Entrega")
	dataPrevisaoRetorno = models.DateTimeField("Data de Previsão do Retorno")
	dataRetorno = models.DateTimeField("Data Retorno", null=True, blank=True)
	usuario = models.ForeignKey(User, related_name='usuario', null=True, blank=True)
	responsavel = models.ForeignKey('pessoa.Pessoa', related_name='responsavel')
	propriedade = models.ForeignKey('propriedade.Propriedade')
	molhos = models.ManyToManyField('molho.Molho')
	
	def __str__(self):
		return str(self.usuario.username)