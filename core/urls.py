from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'propriedade/', include('propriedade.urls', namespace="propriedade")),
    url(r'proprietario/', include('pessoa.urls', namespace="proprietario")),

]
