from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'saida$', views.saida, name='saida'),
    url(r'devolucao/(?P<pk>[0-9]+)/$', views.devolucao, name='devolucao'),
    url(r'search/$', views.SearchFilter.as_view(), name='search-filter'),
    url(r'deletar/(?P<pk>[0-9]+)/$', views.DeleteRegistro.as_view(), name='delete'),
    url(r'update/(?P<pk>[0-9]+)/$', views.update, name='update'),
    url(r'getmolhos/(?P<pk>[0-9]+)/$', views.getmolhos, name='getmolhos'),
]
