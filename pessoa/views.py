from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ProprietarioForm, PessoaForm
from pessoa.models import Pessoa
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

def pessoahome(request):
    return render(request, 'pessoa/pessoahome.html')

def pessoacreate(request):
    form = PessoaForm()
    context = {
        'form': form,
        'objeto': 'Pessoa',
    }

    return render(request, 'form.html', context)
