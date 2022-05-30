from dataclasses import fields
from django import forms
from .models import Contas_Pagar

class ContaPagarForm(forms.ModelForm):
    class Meta:
        model = Contas_Pagar
        fields = ['fornecedor', 'data_vencimento', 'pago', 'ids_notas_fiscais']