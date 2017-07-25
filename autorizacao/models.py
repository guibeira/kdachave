from django.db import models

# Create your models here.
class Autorizacao (models.Model):
    autorizada = models.ForeignKey('pessoa.Pessoa')
    criador = models.ForeignKey('pessoa.Pessoa', related_name='creator')
    propriedade = models.ForeignKey('propriedade.Propriedade')
    descricao = models.TextField()
    dataInicio = models.DateTimeField()
    dataFim = models.DateTimeField()
    dataCriacao = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10)

class Registro(models.Model):
    molho = models.ForeignKey('molho.Molho')
    autorizacao = models.ForeignKey('Autorizacao')
    status = models.CharField(max_length=100)
    dataRetirada = models.DateTimeField()
    dataDevolucao = models.DateTimeField()
    recebidoPor = models.ForeignKey('pessoa.Pessoa',related_name='recebido_por')
    descricao = models.TextField()
    autorizadoPor = models.ForeignKey('pessoa.Pessoa', related_name='entregue_por')

class Confirmacao(models.Model):
    data = models.DateTimeField()
    registro = models.ForeignKey('Registro')
    chave = models.ForeignKey('molho.Chave')
    controle = models.ForeignKey('molho.Controle')
    status = models.CharField(max_length=20)
    conferente = models.ForeignKey('pessoa.Pessoa')
