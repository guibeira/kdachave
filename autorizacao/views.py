from django.shortcuts import render, get_object_or_404
from .models import Autorizacao
from .forms import AutorizacaoForm

@login_required
def create(request, pk):
    propriedade = get_object_or_404(Propriedade,pk=pk)
    if request.method == "POST":
        form = AutorizacaoForm(request.POST)
        if form.is_valid():
            autorizacao = form.save(commit=False)
            autorizacao.propriedade = propriedade
            autorizacao.save()
            return redirect('propriedade:detalhe',propriedade.pk)
        else:
            context = {
                'form': form ,
            }
            return render(request, 'autorizacao/form.html', context)
    else:
        form = AutorizacaoForm()
        context = {
            'form': form,
        }
        return render(request, 'autorizacao/form.html', context)

@login_required
def update(request, pk):
    autorizacao = get_object_or_404(Autorizacao,pk=pk)
    if request.method == "POST":
        form = AutorizacaoForm(request.POST, instance=autorizacao)
        if form.is_valid():
            autorizacao.save()
            return redirect('propriedade:detalhe',autorizacao.propriedade.pk)
        else:
            context = {
                'form': form ,
            }
            return render(request, 'autorizacao/form.html', context)
    else:
        form = AutorizacaoForm(instance=autorizacao)
        context = {
            'form': form,
        }
        return render(request, 'autorizacao/form.html', context)

def delete_autorizacao(request,pk):
    autorizacao = get_object_or_404(Autorizacao,pk=pk)
    propriedade = autorizacao.propriedade
    autorizacao.delete()
    return redirect('propriedade:detalhe', propriedade.pk)
