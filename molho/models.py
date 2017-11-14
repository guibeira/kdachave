from django.db import models

# Create your models here.
class Molho(models.Model):
    descricao = models.CharField(max_length=150)
    chaves = models.ManyToManyField('Chave')
    controle = models.ManyToManyField('Controle')

class Chave (models.Model):
    descricao = models.TextField()

class Controle (models.Model):
    descricao = models.TextField()