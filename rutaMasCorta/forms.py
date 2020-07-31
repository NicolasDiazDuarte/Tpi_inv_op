from django import forms
from .models import Source,Target,Weight

class SourceForm(forms.ModelForm):
    class Meta:
        model= Source
        fields = ['source']
    

class TargetForm(forms.ModelForm):
    class Meta:
        model= Target
        fields = ['target']
        
class WeightForm(forms.ModelForm):
    class Meta:
        model= Weight
        fields = ['weightnro']
