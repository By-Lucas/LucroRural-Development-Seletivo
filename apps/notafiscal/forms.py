from django import forms
from .models import Csv_notas, Nota_Fiscal

class CsvNotaForm(forms.ModelForm):
    class Meta:
        model = Csv_notas
        fields = ('file_name',)

class NotaFiscalForm(forms.ModelForm):
    class Meta:
        model = Nota_Fiscal
        fields = [
            'numero_da_conta', 
            'fornecedor', 
            'nome_produto', 
            'categoria', 
            'quantidade,',
            'valor_total'
            ]
