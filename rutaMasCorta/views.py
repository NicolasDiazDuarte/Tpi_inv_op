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

def instanciarArreglos(flag):
    global arrNodoOrigen
    global arrNodoDestino
    global arrPeso
    
    arrNodoDestino = []
    arrNodoOrigen = []
    arrPeso = []
    flag = False

    
        
        
def CargarArreglos():
    print('todo good')
    #usar try catch 
    # if exists 
    #probar con base de datos primero sino solo con arreglos 

def instanciarNodos(request):
    global arrNodoOrigen
    global arrNodoDestino
    global arrPeso
    global flag
    
    
    source_form = SourceForm(request.POST or None)
    target_form = TargetForm(request.POST or None)
    weight_form = WeightForm(request.POST or None)
    if request.method== 'POST':
        source_form = SourceForm(request.POST )
        target_form = TargetForm(request.POST )
        weight_form = WeightForm(request.POST )
    if flag == True:
        instanciarArreglos(flag)
        
       
    if source_form.is_valid() and target_form.is_valid() and weight_form.is_valid():
        for key,value in request.POST.items():
            if key != 'csrfmiddlewaretoken':
                if key == "Peso" :
                    arrPeso.append(value)
                else:
                    if key == "Nodo Origen":
                        arrNodoOrigen.append(value)
                    else:
                        arrNodoDestino.append(value)

        print(arrPeso)      
        return render(request,'rutaMasCorta.html',{'source_form':source_form,'target_form':target_form,'weight_form':weight_form,'arrPeso':arrPeso})
    else:
        source_form=SourceForm()
        target_form=TargetForm()
        weight_form=WeightForm()
    return render(request,'rutaMasCorta.html',{'source_form':source_form,'target_form':target_form,'weight_form':weight_form})
        