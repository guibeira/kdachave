from django.conf.urls import url, include
from apps.pessoa import views

urlpatterns = [
    url(r'^$', views.pessoahome, name='home'),
    url(r'criar$', views.pessoacreate, name='create'),
    url(r'atualizar/(?P<pk>[0-9]+)$', views.pessoaUpdate, name='update'),
    url(r'deletar/(?P<pk>[0-9]+)/$', views.DeletePessoa.as_view(), name='delete'),
    url(r'lista-usuarios$', views.listUsers, name='listUsers'),
    url(r'criar-usuario$', views.createUser, name='createUser'),
    url(r'atualizar-usuario/(?P<pk>[0-9]+)$', views.updateUser, name='updateUser'),
    url(r'deletar-usuario/(?P<pk>[0-9]+)/$', views.DeleteUser.as_view(), name='deleteUser'),
	url(r'resetar-senha$', views.change_password, name='password_change'),
]
