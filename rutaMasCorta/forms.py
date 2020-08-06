from django import forms
from .models import Rows,Nodos,Lista


class RowsForm(forms.ModelForm):
    class Meta:
        model= Rows
        fields = ['rows',]

class NodosForm(forms.ModelForm):
    class Meta:
        model= Nodos
        fields = ['source','target','weight',]    


