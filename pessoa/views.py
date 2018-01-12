from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from .forms import PessoaForm, UserForm, UserWithoutPasswordForm
from pessoa.models import Pessoa
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

@login_required
def pessoaUpdate(request, pk):
    pessoa = get_object_or_404(Pessoa,pk=pk)
    if request.method == 'POST':
        form = PessoaForm(request.POST, instance=pessoa)
        context = {
            'form': form,
            'objeto': 'Pessoa',
        }
        if form.is_valid():
            p1 = form.save()
            return redirect('pessoa:home')
        else:
            return render(request, 'form.html', context)
    else:
        form = PessoaForm(instance=pessoa)
        context = {
            'form': form,
            'objeto': 'Pessoa',
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
        context = {
            'form': form,
            'objeto': 'Pessoa',
        }
        if form.is_valid():
            p1 = form.save()
            return redirect('pessoa:home')
        else:
            return render(request, 'form.html', context)
    else:
        form = PessoaForm()
        context = {
            'form': form,
            'objeto': 'Pessoa',
        }
        return render(request, 'form.html', context)

@login_required
def listUsers(request):
    users = User.objects.all()
    context = {
        'users':users,
    }
    return render(request, 'pessoa/users.html', context)

@login_required
def createUser(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        context = {
            'form': form,
            'objeto': 'User',
        }
        if form.is_valid():
            password = form.cleaned_data['password']
            user = form.save()
            user.set_password(password)
            user.save()
            return redirect('pessoa:listUsers')
        else:
            return render(request, 'form.html', context)
    else:
        form = UserForm()
        context = {
            'form': form,
            'objeto': 'User',
        }
        return render(request, 'form.html', context)

@login_required
def updateUser(request,pk):
    usuario = get_object_or_404(User,pk=pk)
    if request.method == 'POST':
        form = UserWithoutPasswordForm(request.POST, instance=usuario)
        context = {
            'form': form,
            'objeto': 'User',
        }
        if form.is_valid():
            user = form.save()
            return redirect('pessoa:listUsers')
        else:
            return render(request, 'form.html', context)
    else:
        form = UserWithoutPasswordForm(instance=usuario)
        context = {
            'form': form,
            'objeto': 'User',
        }
        return render(request, 'form.html', context)

class DeleteUser(LoginRequiredMixin, DeleteView):
    model = User
    success_url = reverse_lazy('pessoa:listUsers')
    template_name = 'confirmdelete.html'

@login_required
def change_password(request):
    print('RESET PASSWORD')
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('pessoa:listUsers')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form
    }
    return render(request, "pessoa/reset-password.html", context)