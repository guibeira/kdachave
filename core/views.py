from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from registro.forms import RegistroForm
from registro.models import Registro
from molho.models import Molho

@login_required
def index(request):
	registros = Registro.objects.all().order_by('dataPrevisaoRetorno')
	countEmUso = Molho.objects.filter(status=0).count()
	countDevolvidos = Molho.objects.filter(status=1).count()
	countAlerta = Molho.objects.filter(status=2).count()
	countPerdido = Molho.objects.filter(status=3).count()

	context = {
				'countEmUso' : countEmUso,
				'countDevolvidos' : countDevolvidos,
				'countAlerta' : countAlerta,
				'countPerdido' : countPerdido,
				'registros'  : registros,
			}
	return render(request, "index2.html", context)

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