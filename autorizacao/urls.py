from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'create/(?P<pk>[0-9]+)/$', views.create, name='create'),
    url(r'delete/(?P<pk>[0-9]+)/$', views.delete_autorizacao, name='delete'),
    url(r'getbypropriedade/(?P<pk>[0-9]+)/$', views.get_autorizacao_by_propriedade, name='getbypropriedade'),
    url(r'update/(?P<pk>[0-9]+)/$', views.update_autorizacao, name='update'),
]
