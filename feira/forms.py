from django import forms
from .models import Bancas, Leitura

class BancasForms(forms.ModelForm):
    class Meta:
        model = Bancas
        fields = ['qtd', 'numero']



class LeituraForms(forms.ModelForm):
    class Meta:
        model = Leitura
        fields = '__all__'
        