from django.conf.urls import url, include
from . import views
from django.contrib.auth import views as auth_views
from pessoa import views as pessoaview

urlpatterns = [
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'},name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^$', views.index, name='home'),
    url(r'propriedade/', include('propriedade.urls', namespace="propriedade")),
    url(r'proprietario/', include('pessoa.urls.proprietario', namespace="proprietario")),
    url(r'pessoa/', include('pessoa.urls.pessoa', namespace="pessoa")),
    url(r'autorizacao/', include('autorizacao.urls', namespace="autorizacao")),
    url(r'molho/', include('molho.urls', namespace="molho")),
]
