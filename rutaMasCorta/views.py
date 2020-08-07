from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import RowsForm, NodosForm
from .models import Rows


# Create your views here.

def index(request):
    
    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'index.html',
        context={},
    )


def instanciarNodosRMC(request):
    if request.method == 'POST':
        rows=RowsForm(request.POST)

        if rows.is_valid():
            
            value = rows.cleaned_data['rows']

            for i in range(value):
                globals()['nodos{}'.format(i)] = NodosForm(request.POST)
            
            return render(request,'rutaMasCorta.html',{'rows':rows, 'nodos1':nodos1})
    else:
        rows=RowsForm()
    return render(request,'rutaMasCorta.html',{'rows':rows})
        