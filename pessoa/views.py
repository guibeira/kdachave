from django.shortcuts import render
from .forms import ProprietarioForm, PessoaForm
# Create your views here.

def proprietariohome(request):
    return render(request, 'pessoa/proprietariohome.html')

def proprietariocreate(request):
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
