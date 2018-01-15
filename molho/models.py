from django.db import models

# Create your models here.
class Molho(models.Model):
	descricao = models.CharField(max_length=150)
	chaves = models.IntegerField('Quantidade de Chaves')
	controles = models.IntegerField('Quantidade de Controle')
	propriedade = models.ForeignKey('propriedade.Propriedade')
	STATUS =(
	            (0, 'Em Uso'),
	            (1, 'Devolvido'),
	            (2, 'Alerta'),
	            (3, 'Perdido'),
            )
	status = models.IntegerField("Status do Molho",
                                    choices=STATUS,
                                    blank=True,
                                    null=True,
                                )
	def __str__(self):
		return self.descricao