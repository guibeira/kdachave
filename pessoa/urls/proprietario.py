
from django.conf.urls import url, include
from pessoa import views

urlpatterns = [
    url(r'^$', views.proprietario_home, name='home'),
    url(r'create$', views.proprietario_create, name='create'),
    url(r'update/(?P<pk>[0-9]+)$', views.propietario_update, name='update'),
    url(r'deletar/(?P<pk>[0-9]+)/$', views.DeleteProprietatio.as_view(), name='delete'),
]
