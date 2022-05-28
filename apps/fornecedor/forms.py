from django import forms
from .models import Csv, Fornecedor


class CsvForm(forms.ModelForm):
    class Meta:
        model = Csv
        fields = ('file_name',)


class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = ['nome', 'cnpj', 'telefone']