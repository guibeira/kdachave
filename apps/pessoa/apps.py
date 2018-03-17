from django.apps import AppConfig


class PessoaConfig(AppConfig):
    name = 'apps.pessoa'
    verbose_name = 'Pessoa'
    
    def ready(self):
        import apps.pessoa.signals
