
from django.conf.urls import url, include
from pessoa import views

urlpatterns = [
    url(r'^$', views.proprietariohome, name='home'),
    url(r'/create$', views.proprietariocreate, name='create'),
    url(r'/update/(?P<pk>[0-9]+)$', views.ProprietatioUpdate.as_view(), name='update'),
    url(r'/deletar/(?P<pk>[0-9]+)/$', views.DeleteProprietatio.as_view(), name='delete'),

]
   