from django.shortcuts import render, redirect, get_object_or_404
from .forms import PropriedadeForm
from .models import Propriedade
from molho.models import Molho
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin

@login_required
def home(request):
    propriedades = Propriedade.objects.all()
    context = {
        'propriedades' : propriedades,
    }
    return render(request, 'propriedade/home.html', context)


@login_required
def create(request):
    if request.method == "POST":
        form = PropriedadeForm(request.POST)
        if form.is_valid():
            propriedade = form.save()
            propriedade.save()
            return redirect('propriedade:home')

        else:
            context = {
                'form': form ,
            }
            return render(request, 'form.html', context)
    else:
        form = PropriedadeForm()
        context = {
            'form': form,
            'objeto' : 'Propriedade',
        }
        return render(request, 'form.html', context)


def detalhes(request, pk):
    propriedade = get_object_or_404(Propriedade,pk=pk)
    molhos = Molho.objects.filter(propriedade_id=propriedade.pk)
    context = {
        "propriedade":propriedade,
        "molhos": molhos,
    }
    return render(request, 'propriedade/detail.html', context)

def updatePropriedade(request, pk):
    propriedade = get_object_or_404(Propriedade,pk=pk)
    if request.method == 'POST':
        form = PropriedadeForm(request.POST, instance=propriedade)
        if form.is_valid():
            p1 = form.save()
            return redirect('propriedade:home')
        else:
            context = {
                'form' :form,
                'objeto': 'Propriedade',
            }
            return render(request, 'form.html', context)
    else:
        form = PropriedadeForm(instance=propriedade)
        context = {
            'form': form,
            'objeto': 'Propriedade',
        }

        return render(request, 'form.html', context)


class DeletePropriedade(LoginRequiredMixin, DeleteView):
    model = Propriedade
    success_url = reverse_lazy('propriedade:home')
    template_name = 'confirmdelete.html'