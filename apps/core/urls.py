from django.conf.urls import url, include
from . import views
from django.contrib.auth import views as auth_views
from apps.pessoa import views as pessoaview

urlpatterns = [
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'},name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^$', views.index, name='home'),
    url(r'^filtro/$', views.registro_filter, name='filter'),
    url(r'propriedade/', include('apps.propriedade.urls', namespace="propriedade")),
    url(r'pessoa/', include('apps.pessoa.urls.pessoa', namespace="pessoa")),
    url(r'molho/', include('apps.molho.urls', namespace="molho")),
    url(r'registro/', include('apps.registro.urls', namespace="registro")),
    url(r'updateDashboard/', views.updateDashboard , name="updateDashboard"),
]
