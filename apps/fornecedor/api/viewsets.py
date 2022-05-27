from rest_framework import viewsets

from fornecedor.api.serializres import  Fornecedor_serializer
from fornecedor.models import Fornecedor

# segue padrao dos outros junto com as bibliotecas importadas
class  Fornecedor_viresets(viewsets.ModelViewSet):
    queryset = Fornecedor.objects.all().order_by('data_cadastro')
    serializer_class = Fornecedor_serializer