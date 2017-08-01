from django.shortcuts import render
from django.http import HttpResponse
from .forms import ProprietarioForm, PessoaForm
# Create your views here.

def proprietariohome(request):
    return render(request, 'pessoa/proprietariohome.html')

def proprietariocreate(request):
    if request.method == 'POST':
        form = ProprietarioForm(request.POST)
        if form.is_valid():
            print('formulário valido')
        else:
            print('deu ruim')
        return HttpResponse(status=200)
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
