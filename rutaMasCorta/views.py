from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import TargetForm,SourceForm,WeightForm
from .models import Source,Target,Weight


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
        source= SourceForm(request.POST )
        target = TargetForm(request.POST )
        weight = WeightForm(request.POST )

        if source.is_valid() and target.is_valid() and weight.is_valid():
            
            dataTarget = target.cleaned_data['Nodo_Destino']
            dataSource = source.cleaned_data['Nodo_Origen']
            dataWeight = weight.cleaned_data['Peso']
        
            return render(request,'rutaMasCorta.html',{'source':source,'target':target,'weight':weight})
    else:
        source=SourceForm()
        target=TargetForm()
        weight=WeightForm()
    return render(request,'rutaMasCorta.html',{'source':source,'target':target,'weight':weight})
        