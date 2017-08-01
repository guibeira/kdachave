from django.shortcuts import render
from .forms import ProprietarioForm
# Create your views here.
def create(request):
    form = ProprietarioForm()
    context = {
        'form': form,
        'objeto': 'Proprietario',
    }

    return render(request, 'form.html', context)