from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import RowsForm
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
    if request.method== 'POST':
        rows=RowsForm(request.POST)

        if rows.is_valid():
            
            print("todo good")
        
            #return render(request,'rutaMasCorta.html',{'source':source,'target':target,'weight':weight})
    else:
        rows=RowsForm()
    return render(request,'rutaMasCorta.html',{'rows':rows})
        