from django.shortcuts import render, redirect
from .forms import PropriedadeForm
from .models import Propriedade
from django.core.urlresolvers import reverse_lazy
from endereco.forms import EnderecoForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.

@login_required
def home(request):
    propriedades = Propriedade.objects.all()
    context = {
        'propriedades' : propriedades,
    }
    return render(request, 'propriedade/home.html', context)


@login_required
def create(request):
    if request.method == "POST":
        form = PropriedadeForm(request.POST)
        endereco = EnderecoForm(request.POST)
        if form.is_valid() and endereco.is_valid():
            propriedade = form.save()
            endereco = endereco.save()
            propriedade.endereco = endereco
            propriedade.save()
            return redirect('propriedade:home')

        else:
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

class DeletePropriedade(DeleteView):
    print('caiu aqui');
    model = Propriedade
    success_url = reverse_lazy('propriedade:home')
    template_name = 'confirmdelete.html'