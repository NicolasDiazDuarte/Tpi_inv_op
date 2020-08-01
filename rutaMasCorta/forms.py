from django import forms
from .models import Source,Target,Weight

class SourceForm(forms.ModelForm):
    class Meta:
        model= Source
        fields = ['Nodo_Origen']
    

class TargetForm(forms.ModelForm):
    class Meta:
        model= Target
        fields = ['Nodo_Destino']
        
class WeightForm(forms.ModelForm):
    class Meta:
        model= Weight
        fields = ['Peso']
