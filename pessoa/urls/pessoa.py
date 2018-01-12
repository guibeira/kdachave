from django.conf.urls import url, include
from pessoa import views

urlpatterns = [
    url(r'^$', views.pessoahome, name='home'),
    url(r'create$', views.pessoacreate, name='create'),
    url(r'update/(?P<pk>[0-9]+)$', views.pessoaUpdate, name='update'),
    url(r'deletar/(?P<pk>[0-9]+)/$', views.DeletePessoa.as_view(), name='delete'),
    url(r'listUsers$', views.listUsers, name='listUsers'),
    url(r'createUser$', views.createUser, name='createUser'),
    url(r'updateUser/(?P<pk>[0-9]+)$', views.updateUser, name='updateUser'),
    url(r'deleteUser/(?P<pk>[0-9]+)/$', views.DeleteUser.as_view(), name='deleteUser'),
	url(r'password-reset$', views.change_password, name='password_change'),
]