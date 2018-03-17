from django.apps import AppConfig


class RegistroConfig(AppConfig):
    name = 'apps.registro'

    def ready(self):
        import apps.registro.signals
