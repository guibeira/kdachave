from django.apps import AppConfig


class RegistroConfig(AppConfig):
    name = 'registro'

    def ready(self):
        import registro.signals
