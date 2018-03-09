from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Registro


@receiver(post_save, sender=Registro)
def model_post_save(sender, **kwargs):
    STATUS = {
        'não devolvido': 0,
        'devolvido': 1,
        'atrasado': 2,
    }
    registro = kwargs['instance']
    for molho in registro.molhos.all():
        molho.status = STATUS[registro.status]
        molho.save()
