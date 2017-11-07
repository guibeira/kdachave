from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.dispatch import receiver
from django.conf import settings
from .models import Pessoa
import os.path




@receiver(pre_save, sender=Pessoa)
@receiver(pre_save, sender=Pessoa)
def model_pre_change(sender, **kwargs):
    if os.path.isfile(settings.READ_ONLY_FILE):
        raise ReadOnlyException('Model in read only mode, cannot save')



@receiver(post_delete, sender=Pessoa)
def model_post_save(sender, **kwargs):
    # print('no signal do pessoa')
    print(kwargs['instance'])
    pessoa = kwargs['instance']
    if not pessoa.proprietario:
        pessoa.user.delete()
