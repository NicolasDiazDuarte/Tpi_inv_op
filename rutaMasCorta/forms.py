from django import forms
from .models import Source,Target,Weight

class SourceForm(forms.ModelForm):
    class Meta:
        model= Autor
        fields = ['source']

class TargetForm(forms.ModelForm):
    class Meta:
        model= Autor
        fields = ['target']
        
class WeightForm(forms.ModelForm):
    class Meta:
        model= Autor
        fields = ['weightnro']
