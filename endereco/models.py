from django.db import models

# Create your models here.
class Endereco(models.Model):
    cep = models.CharField(max_length=9)
    logradouro = models.TextField()
    cidade = models.CharField(max_length=30)
    estado = models.CharField(max_length=2)