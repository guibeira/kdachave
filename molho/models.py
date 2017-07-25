from django.db import models

# Create your models here.
class Molho(models.Model):
    chaves = models.ManyToManyField('Chave')
    chaves = models.ManyToManyField('Controle')

class Chave (models.Model):
    descricao = models.TextField()

class Controle (models.Model):
    descricao = models.TextField()