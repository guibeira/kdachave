from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timezone
now = datetime.now(timezone.utc)


class Registro(models.Model):
    dataEntrega = models.DateTimeField("Data Entrega")
    dataPrevisaoRetorno = models.DateTimeField("Data de Previsão do Retorno")
    dataRetorno = models.DateTimeField("Data Retorno", null=True, blank=True)
    usuario = models.ForeignKey(
        User, related_name='usuario', null=True, blank=True
    )
    responsavel = models.ForeignKey(
        'pessoa.Pessoa', related_name='responsavel'
    )
    propriedade = models.ForeignKey('propriedade.Propriedade')
    molhos = models.ManyToManyField('molho.Molho')

    @property
    def status(self):
        if self in atrasados():
            return 'atrasado'
        elif self in devolvidos():
            return 'devolvido'
        elif self in nao_devolvidos():
            return 'não devolvido'
        else:
            'erro'

    def __str__(self):
        return str(self.usuario.username)


def atrasados():
    registros = Registro.objects.filter(
        dataRetorno__isnull=True, dataPrevisaoRetorno__lt=now
    ).order_by('dataPrevisaoRetorno')
    return registros


def devolvidos():
    registros = Registro.objects.filter(
        dataRetorno__isnull=False,
    ).order_by('dataPrevisaoRetorno')
    return registros


def nao_devolvidos():
    registros = Registro.objects.filter(
        dataRetorno__isnull=True, dataPrevisaoRetorno__gte=now
    ).order_by('dataPrevisaoRetorno')
    return registros
