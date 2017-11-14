from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
from .models import Autorizacao
from propriedade.models import Propriedade
from .forms import AutorizacaoForm


@login_required
def get_autorizacao_by_propriedade(request, pk):
    template_name = 'autorizacao/get_autorizacao_by_propriedade.html'
    autorizacoes = Autorizacao.objects.filter(propriedade_id=pk)
    context = {
        'autorizacoes' : autorizacoes
    }
    return render(request, template_name, context)

@login_required
def create(request, pk):
    propriedade = get_object_or_404(Propriedade,pk=pk)
    if request.method == "POST":
        form = AutorizacaoForm(request.POST)
        if form.is_valid():
            autorizacao = form.save(commit=False)
            autorizacao.propriedade = propriedade
            autorizacao.save()
            return HttpResponse(200);
        else:
            context = {
                'form': form,
            }
            return render(request, 'autorizacao/form.html', context, status=500)
    else:
        form = AutorizacaoForm()
        context = {
            'form': form,
        }
        return render(request, 'autorizacao/form.html', context)

@login_required
def update_autorizacao(request, pk):
    autorizacao = get_object_or_404(Autorizacao,pk=pk)
    if request.method == "POST":
        form = AutorizacaoForm(request.POST, instance=autorizacao)
        if form.is_valid():
            print("isvalid")
            form.save()
            return HttpResponse(200);
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

@login_required
def delete_autorizacao(request,pk):
    autorizacao = get_object_or_404(Autorizacao,pk=pk)
    propriedade = autorizacao.propriedade
    autorizacao.delete()
    return HttpResponse(200);
