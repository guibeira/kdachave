from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from .forms import ProprietarioForm, PessoaForm
from pessoa.models import Pessoa
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.

def proprietariohome(request):
    proprietarios = Pessoa.objects.filter(proprietario=True)
    context = {
        'proprietarios' : proprietarios
    }
    return render(request, 'pessoa/proprietariohome.html', context )

def proprietariocreate(request):
    if request.method == 'POST':
        form = ProprietarioForm(request.POST)
        if form.is_valid():
            pessoa = form.save()
            pessoa.proprietario = True
            pessoa.save()
            return redirect('proprietariohome')
        else:
            return render(request, 'form.html', {'form': form})
    else:
        form = ProprietarioForm()
        context = {
            'form': form,
            'objeto': 'Proprietario',
        }
        return render(request, 'form.html', context)

class ProprietatioUpdate(UpdateView):
    model = Pessoa
    form_class = ProprietarioForm
    template_name = 'form.html'
    success_url = reverse_lazy('proprietariohome')

def pessoahome(request):
    return render(request, 'pessoa/pessoahome.html')

def pessoacreate(request):
    form = PessoaForm()
    context = {
        'form': form,
        'objeto': 'Pessoa',
    }

    return render(request, 'form.html', context)
