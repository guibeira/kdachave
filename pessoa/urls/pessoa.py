from django.conf.urls import url, include
from pessoa import views

urlpatterns = [
    # url(r'^$', views.home, name='home'),
    # url(r'create$', views.create, name='create'),
     url(r'^$', views.pessoahome, name='home'),
    url(r'create$', views.pessoacreate, name='create'),
    url(r'update/(?P<pk>[0-9]+)$', views.pessoaUpdate, name='update'),
    url(r'deletar/(?P<pk>[0-9]+)/$', views.DeletePessoa.as_view(), name='delete'),

]
