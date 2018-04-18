from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'criar/(?P<pk>[0-9]+)/$', views.create, name='create'),
    url(r'deletar/(?P<pk>[0-9]+)/$', views.DeleteMolho.as_view(), name='delete'),
    url(r'search-molho/$', views.MolhoSearch.as_view(), name='searchmolho'),
    url(r'getmolhobypropriedade/(?P<pk>[0-9]+)/$', views.get_molho_by_propriedade, name='getmolhobypropriedade'),
    url(r'update/(?P<pk>[0-9]+)/$', views.update_molho, name='update'),
    url(r'updateStatus/(?P<pk>[0-9]+)/(?P<statusId>[0-9]+)/$', views.update_status, name='updateStatus'),

]
