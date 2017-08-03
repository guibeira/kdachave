from django.shortcuts import render, redirect
from .forms import PropriedadeForm
from endereco.forms import EnderecoForm
# Create your views here.
def home(request):

    return render(request, 'propriedade/home.html')

def create(request):

    if request.method == "POST":
        form = PropriedadeForm(request.POST)
        endereco = EnderecoForm(request.POST)
        if form.is_valid() and endereco.is_valid():
            print('formulário lindão')
            propriedade = form.save()
            endereco = endereco.save()
            propriedade.endereco = endereco
            propriedade.save()
            return redirect('propriedade:home')

        else:
            print('formulário cagado')
            context = {
                'form': form ,
                'endereco': endereco
            }
            return render(request, 'propriedade/propriedade_form.html', context)
    else:
        form = PropriedadeForm()
        endereco = EnderecoForm()
        context = {
            'form': form, 
            'endereco' : endereco,
            'objeto' : 'Propriedade',
        }
        return render(request, 'propriedade/propriedade_form.html', context)