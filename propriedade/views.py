from django.shortcuts import render
from .forms import PropriedadeForm
# Create your views here.
def home(request):

    return render(request, 'propriedade/home.html')

def create(request):
    form = PropriedadeForm()
    context = {
        'form': form
    }
    return render(request, 'propriedade/form.html', context)