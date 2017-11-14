from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'create/(?P<pk>[0-9]+)/$', views.create, name='create'),
    url(r'delete/(?P<pk>[0-9]+)/$', views.delete_molho, name='delete'),
    url(r'getmolhobypropriedade/(?P<pk>[0-9]+)/$', views.get_molho_by_propriedade, name='getmolhobypropriedade'),
    url(r'update/(?P<pk>[0-9]+)/$', views.update_molho, name='update'),
]

