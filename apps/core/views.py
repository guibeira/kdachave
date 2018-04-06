from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from apps.registro.models import Registro, atrasados, devolvidos, nao_devolvidos
from json_views.views import JSONDataView
from apps.molho.models import Molho


@login_required
def registro_filter(request):
	filtro = request.POST.get('filter_by')
	template_name = 'tabela.html'

	if filtro not in ['atrasados', 'adevolder', 'devolvidos']:
		return Http404
	if filtro == 'atrasados':
		registros = atrasados()
	elif filtro == 'adevolder':
		registros = nao_devolvidos()
	elif filtro == 'devolvidos':
		registros = devolvidos()

	context={
		'registros': registros
		}
	return render(request, template_name, context)


class Index(LoginRequiredMixin, TemplateView):
	template_name = 'index.html'


class TotaisRegitro(LoginRequiredMixin, JSONDataView):

	def get_context_data(self, **kwargs):
		context = super(TotaisRegitro, self).get_context_data(**kwargs)
		context['atrasados'] = atrasados().count()
		context['devolvidos'] = devolvidos().count()
		context['nao_devolvidos'] = nao_devolvidos().count()
		return context


@login_required
def updateDashboard(request):

	countEmUso = Molho.objects.filter(status=0).count()
	countDevolvidos = Molho.objects.filter(status=1).count()
	countAlerta = Molho.objects.filter(status=2).count()
	countPerdido = Molho.objects.filter(status=3).count()

	context = {
				'countEmUso' : countEmUso,
				'countDevolvidos' : countDevolvidos,
				'countAlerta' : countAlerta,
				'countPerdido' : countPerdido,
			}

	return render(request, "dashboard_molhos.html", context)
