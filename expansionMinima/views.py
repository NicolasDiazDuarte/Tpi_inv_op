from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import TargetForm,SourceForm,WeightForm

# Create your views here.

def index(request):
    
    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'index.html',
        context={},
    )

def instanciarNodosEM(request):
    if request.method== 'POST':
        source_form = SourceForm(request.POST)
        target_form = TargetForm(request.POST)
        weight_form = WeightForm(request.POST)
        if source_form.is_valid() and target_form.is_valid() and weight_form.is_valid():
            print('esta bien')
            return redirect('expansionMinima.html')
    else:
        source_form=SourceForm()
        target_form=TargetForm()
        weight_form=WeightForm()
    return render(request,'expansionMinima.html',{'source_form':source_form,'target_form':target_form,'weight_form':weight_form})
        