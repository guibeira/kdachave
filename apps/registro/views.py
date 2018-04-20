from django.shortcuts import render, redirect, get_object_or_404
from django.forms import modelformset_factory
from .forms import RegistroForm, RegistroSaidaGetForm, RegistroSaidaPostForm, RegistroDevolucaoForm
from .models import Registro
from django.views.generic import UpdateView
from django.http import JsonResponse, HttpResponse
from django.urls import reverse
from apps.propriedade.models import Propriedade
from apps.molho.models import Molho
from apps.molho.forms import MolhoBulkEdition
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin


class SearchFilter(LoginRequiredMixin, ListView):
    template_name = 'tabela.html'
    model = Registro
    context_object_name = "registros"

    def get_queryset(self, *args, **kwargs):
        try:
            resposavel = self.kwargs['resposavel']
        except:
            resposavel = ""
        if (resposavel != ""):
            object_list = self.model.objects.filter(resposavel_name__icontains = name)
        else:
            object_list = self.model.objects.all()
        return object_list


@login_required
def saida(request):
    if request.method == "POST":
        form = RegistroSaidaPostForm(request.POST)
        if form.is_valid():
            registro = form.save()
            registro.usuario = request.user
            registro.save()
            for molho in registro.molhos.all():
                molho.status = 0 # em uso
                molho.save()
            return redirect('home')
        else:
            return JsonResponse(form.errors.as_json(), safe=False, status=500)
    else:
        form = RegistroSaidaGetForm()
        context = {
            'form': form,
            'action': reverse('registro:saida')
        }
        return render(request, 'registro/registro_form.html', context)


@login_required
def update(request, pk):
    registro = get_object_or_404(Registro, pk=pk)

    if request.method == "POST":
        form = RegistroForm(request.POST, instance=registro)
        if form.is_valid():
            registro = form.save()
            return HttpResponse(status=200)
        else:
            context = {
                'form': form,
            }
            return JsonResponse(form.errors.as_json(), safe=False, status=500)
    else:
        form = RegistroForm(instance=registro)
        context = {
            'form': form,
        }
    return render(request, 'registro/registro_form.html', context)


@login_required
def getmolhos(request, pk):
    propriedade = get_object_or_404(Propriedade,pk=pk)
    molhos = Molho.objects.filter(propriedade=propriedade).exclude(status__in=(0,2,3));
    context = {
        "molhos": molhos,
    }
    return render(request, 'registro/molhosToSelect.html', context)


@login_required
def devolucao(request, pk):
    registro = get_object_or_404(Registro, pk=pk)
    CartItemFormSet = modelformset_factory(Molho, form=MolhoBulkEdition, extra=0)
    queryset = registro.molhos.all()
    formset = CartItemFormSet(request.POST or None, queryset=queryset)
    template_name = "registro/registro_form_bulk.html"
    if request.method == "POST":
        form = RegistroDevolucaoForm(request.POST, instance=registro)
        if form.is_valid():
            for f in formset:
                if f.is_valid():
                    f.save()
            registro = form.save()
            return redirect('home')
        else:
            context = {
                'form': form,
                'formset': formset
            }
            return JsonResponse(form.errors.as_json(), safe=False, status=500)
    else:
        form = RegistroDevolucaoForm(instance=registro)
        context = {
            'form': form,
            'formset': formset
        }
        return render(request, template_name, context)


# class Devolucao(LoginRequiredMixin, UpdateView):
#     model = Registro
#     form_class = RegistroDevolucaoForm
#     success_url = reverse_lazy('home')
#     template_name = 'registro/registro_form.html'
#
#     def form_invalid(self, form):
#         print('dentro do formulário invalido')
#         if self.request.is_ajax():
#             return self.render_to_json_response(form.errors, status=400)
