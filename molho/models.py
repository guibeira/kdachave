from django.db import models

# Create your models here.
class Molho(models.Model):
	descricao = models.CharField(max_length=150)
	chaves = models.IntegerField('Quantidade de Chaves')
	controles = models.IntegerField('Quantidade de Controle')
	propriedade = models.ForeignKey('propriedade.Propriedade')

	def __str__(self):
		return self.descricao