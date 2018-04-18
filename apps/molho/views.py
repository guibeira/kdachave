from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
from .models import Molho
from apps.propriedade.models import Propriedade
from .forms import MolhoForm
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin


@login_required
def get_molho_by_propriedade(request, pk):
    template_name = 'molho/get_molho_by_propriedade.html'
    molhos = Molho.objects.filter(propriedade_id=pk)
    context = {
        'molhos' : molhos
    }
    return render(request, template_name, context)


@login_required
def create(request, pk):
    propriedade = get_object_or_404(Propriedade, pk=pk)
    if request.method == "POST":
        form = MolhoForm(request.POST)
        if form.is_valid():
            molho = form.save(commit=False)
            molho.propriedade = propriedade
            molho.save()
            return HttpResponse(200);
        else:
            context = {
                'form': form,
            }
            return render(request, 'molho/form.html', context, status=500)
    else:
        form = MolhoForm()
        context = {
            'form': form,
        }
        return render(request, 'molho/form.html', context)


@login_required
def update_molho(request, pk):
    molho = get_object_or_404(Molho,pk=pk)
    if request.method == "POST":
        form = MolhoForm(request.POST, instance=molho)
        if form.is_valid():
            form.save()
            return HttpResponse(200);
        else:
            context = {
                'form': form ,
            }
            return render(request, 'molho/form.html', context)
    else:
        form = MolhoForm(instance=molho)
        context = {
            'form': form,
        }
        return render(request, 'molho/form.html', context)


class DeleteMolho(LoginRequiredMixin, DeleteView):
    model = Molho
    success_url = reverse_lazy('propriedade:home')
    template_name = 'confirmdelete.html'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        propriedade = self.object.propriedade
        self.object.delete()
        return redirect('propriedade:detalhe', pk=propriedade.pk)


class MolhoSearch(LoginRequiredMixin, ListView):
    template_name = 'molho/molhos_filtrados.html'
    model = Molho
    context_object_name = 'molhos'

    def get_queryset(self, *args, **kwargs):

        propriedade = self.request.GET.get('propriedade', None)
        if propriedade is None:
            queryset = self.model.objects.none()
        else:
            queryset = self.model.objects.filter(propriedade_id=propriedade)
        return queryset



def update_status(request, pk, statusId):
    molho = get_object_or_404(Molho,pk=pk)
    molho.status = statusId
    molho.save()
    return HttpResponse(200);
