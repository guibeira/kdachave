from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
from .models import Molho
from propriedade.models import Propriedade
from .forms import MolhoForm


@login_required
def get_molho_by_propriedade(request, pk):
    template_name = 'molho/get_molho_by_propriedade.html'
    molhos = Molho.objects.filter(propriedade_id=pk)
    context = {
        'molhos' : molhos
    }
    return render(request, template_name, context)

@login_required
def create(request, pk):
    print('molho create')
    propriedade = get_object_or_404(Propriedade,pk=pk)
    if request.method == "POST":
        form = MolhoForm(request.POST)
        if form.is_valid():
            molho = form.save(commit=False)
            molho.propriedade = propriedade
            molho.save()
            return HttpResponse(200);
        else:
            context = {
                'form': form,
            }
            return render(request, 'molho/form.html', context, status=500)
    else:
        form = MolhoForm()
        context = {
            'form': form,
        }
        return render(request, 'molho/form.html', context)

@login_required
def update_molho(request, pk):
    molho = get_object_or_404(Molho,pk=pk)
    if request.method == "POST":
        form = MolhoForm(request.POST, instance=molho)
        if form.is_valid():
            form.save()
            return HttpResponse(200);
        else:
            context = {
                'form': form ,
            }
            return render(request, 'molho/form.html', context)
    else:
        form = MolhoForm(instance=molho)
        context = {
            'form': form,
        }
        return render(request, 'molho/form.html', context)

@login_required
def delete_molho(request,pk):
    molho = get_object_or_404(Molho,pk=pk)
    propriedade = molho.propriedade
    molho.delete()
    return HttpResponse(200);
