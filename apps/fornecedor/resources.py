from import_export import resources
from .models import Fornecedor, Csv

class Fornecedor_Resource(resources.ModelResource):
    class Meta:
        model = Fornecedor
        fields = ['id', 'nome', 'cnpj', 'telefone']