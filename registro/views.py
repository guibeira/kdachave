from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistroForm
from .models import Registro
from propriedade.models import Propriedade
from molho.models import Molho
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin

@login_required
def create(request):
	if request.method == "POST":
		form = RegistroForm(request.POST)
		if form.is_valid():
			registro = form.save()
			registro.usuario = request.user
			registro.save()
			for molho in registro.molhos.all():
				molho.status = 0 # em uso
				molho.save()
			return redirect('home')
		else:
			context = {
				'form': form,
			}
			return render(request, 'registro/registro_form.html', context)
	else:
		form = RegistroForm()
		context = {
			'form': form,
		}
		return render(request, 'registro/registro_form.html', context)

@login_required
def update(request, pk):
	registro = get_object_or_404(Registro,pk=pk)
	if request.method == "POST":
		form = RegistroForm(request.POST, instance=registro)
		if form.is_valid() and formMolho.is_valid():
			registro = form.save()
			return redirect('home')
		else:
			context = {
				'form': form ,
			}
			return render(request, 'registro/registro_form.html', context)
	else:
		form = RegistroForm(instance=registro)
		context = {
			'form': form,
		}
		return render(request, 'registro/registro_form.html', context)

class DeleteRegistro(LoginRequiredMixin, DeleteView):
	model = Registro
	success_url = reverse_lazy('home')
	template_name = 'confirmdelete.html'

@login_required
def getmolhos(request, pk):
	propriedade = get_object_or_404(Propriedade,pk=pk)
	molhos = Molho.objects.filter(propriedade=propriedade).exclude(status__in=(0,2,3));
	context = {
		"molhos":molhos,
	}
	return render(request, 'registro/molhosToSelect.html', context)