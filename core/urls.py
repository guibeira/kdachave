from django.conf.urls import url, include
from . import views
from pessoa import views as pessoaview

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'propriedade/', include('propriedade.urls', namespace="propriedade")),

    url(r'proprietario/$', pessoaview.proprietariohome, name='proprietariohome'),
    url(r'proprietario/create$', pessoaview.proprietariocreate, name='proprietariocreate'),
    url(r'pessoa/$', pessoaview.pessoahome, name='pessoahome'),
    url(r'pessoa/create$', pessoaview.pessoacreate, name='pessoacreate'),
    url(r'^proprietario/update/(?P<pk>[0-9]+)$', pessoaview.ProprietatioUpdate.as_view(), name='proprietarioupdate'),
    url(r'^proprietario/deletar/(?P<pk>[0-9]+)/$', pessoaview.DeleteProprietatio.as_view(), name='proprietariodelete'),

]
