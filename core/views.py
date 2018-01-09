from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from registro.forms import RegistroForm
from registro.models import Registro

# Create your views here.
@login_required
def index(request):
	registros = Registro.objects.all()
	context = {
				'registros': registros,
			}
	return render(request, "index2.html", context)
