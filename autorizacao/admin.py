from django.contrib import admin
from .models import Autorizacao, Registro, Confirmacao
# Register your models here.
admin.site.register(Autorizacao)
admin.site.register(Registro)
admin.site.register(Confirmacao)