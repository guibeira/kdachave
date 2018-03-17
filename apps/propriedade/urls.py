from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'criar$', views.create, name='create'),
    url(r'deletar/(?P<pk>[0-9]+)/$', views.DeletePropriedade.as_view(), name='delete'),
    url(r'detalhes/(?P<pk>[0-9]+)/$', views.detalhes, name='detalhe'),
    url(r'atualizar/(?P<pk>[0-9]+)/$', views.updatePropriedade, name='update'),
]
