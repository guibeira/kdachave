from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    user = models.ForeignKey('auth.User')
    telefoneComercial = models.CharField(max_length=100)
    telefoneResidencial = models.CharField(max_length=100)
    celular1 = models.CharField(max_length=100)
    celular2 = models.CharField(max_length=100)
    endereco = models.ForeignKey('endereco.Endereco')
    proprietario = models.BooleanField(default=False)


