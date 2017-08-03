from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from .forms import ProprietarioForm, PessoaForm, UserForm, UserWithoutPasswordForm
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


class DeleteProprietatio(DeleteView):
    model = Pessoa
    success_url = reverse_lazy('proprietariohome')
    template_name = 'confirmdelete.html'

def pessoaUpdate(request, pk):
    pessoa = get_object_or_404(Pessoa,pk=pk)
    if request.method == 'POST':
        form = PessoaForm(request.POST, instance=pessoa)
        userForm = UserWithoutPasswordForm(request.POST, instance=pessoa.user)
        if form.is_valid() and userForm.is_valid():
            user = userForm.save()
            p1 = form.save()
            return redirect('pessoahome')
        else:
            return render(request, 'form.html', {'form': form})
    else:
        form = PessoaForm(instance=pessoa)
        userForm = UserWithoutPasswordForm(instance=pessoa.user)
        context = {
            'form': form,
            'objeto': 'Pessoa',
            'userForm':userForm,
        }

        return render(request, 'form.html', context)


class DeletePessoa(DeleteView):
    model = Pessoa
    success_url = reverse_lazy('pessoahome')
    template_name = 'confirmdelete.html'


def pessoahome(request):
    pessoas = Pessoa.objects.filter(proprietario=False)
    context = {
        'pessoas' : pessoas
    }
    return render(request, 'pessoa/pessoahome.html', context)

def pessoacreate(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        userForm = UserForm(request.POST)
        if form.is_valid() and userForm.is_valid():
            password = userForm.cleaned_data['password']
            user = userForm.save()
            p1 = form.save()
            user.set_password(password)
            user.save()
            p1.user = user
            p1.save()

            return redirect('pessoahome')
        else:
            return render(request, 'form.html', {'form': form})
    else:
        form = PessoaForm()
        userForm = UserForm()
        context = {
            'form': form,
            'objeto': 'Pessoa',
            'userForm':userForm,
        }

        return render(request, 'form.html', context)
