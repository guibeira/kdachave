from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'create/(?P<pk>[0-9]+)/$', views.create, name='create'),
    url(r'delete/(?P<pk>[0-9]+)/$', views.DeleteMolho.as_view(), name='delete'),
    url(r'getmolhobypropriedade/(?P<pk>[0-9]+)/$', views.get_molho_by_propriedade, name='getmolhobypropriedade'),
    url(r'update/(?P<pk>[0-9]+)/$', views.update_molho, name='update'),
    url(r'updateStatus/(?P<pk>[0-9]+)/(?P<statusId>[0-9]+)/$', views.update_status, name='updateStatus'),
    
]