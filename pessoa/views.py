from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from .forms import PessoaForm, UserForm, UserWithoutPasswordForm
from pessoa.models import Pessoa
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

@login_required
def pessoaUpdate(request, pk):
    pessoa = get_object_or_404(Pessoa,pk=pk)
    if request.method == 'POST':
        form = PessoaForm(request.POST, instance=pessoa)
        userForm = UserWithoutPasswordForm(request.POST, instance=pessoa.user)
        context = {
            'form': form,
            'objeto': 'Pessoa',
            'userForm':userForm,
        }
        if form.is_valid() and userForm.is_valid():
            user = userForm.save()
            p1 = form.save()
            return redirect('pessoa:home')
        else:
            return render(request, 'form.html', context)
    else:
        form = PessoaForm(instance=pessoa)
        userForm = UserWithoutPasswordForm(instance=pessoa.user)
        context = {
            'form': form,
            'objeto': 'Pessoa',
            'userForm':userForm,
        }

        return render(request, 'form.html', context)


class DeletePessoa(LoginRequiredMixin, DeleteView):
    model = Pessoa
    success_url = reverse_lazy('pessoa:home')
    template_name = 'confirmdelete.html'

@login_required
def pessoahome(request):
    pessoas = Pessoa.objects.all()
    context = {
        'pessoas' : pessoas
    }
    return render(request, 'pessoa/pessoahome.html', context)

@login_required
def pessoacreate(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        userForm = UserForm(request.POST)
        context = {
            'form': form,
            'objeto': 'Pessoa',
            'userForm':userForm,
        }
        if form.is_valid() and userForm.is_valid():
            password = userForm.cleaned_data['password']
            user = userForm.save()
            p1 = form.save()
            user.set_password(password)
            user.save()

            return redirect('pessoa:home')
        else:
            return render(request, 'form.html', context)
    else:
        form = PessoaForm()
        userForm = UserForm()
        context = {
            'form': form,
            'objeto': 'Pessoa',
            'userForm':userForm,
        }

        return render(request, 'form.html', context)
