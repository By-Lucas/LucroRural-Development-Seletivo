from rest_framework import viewsets

from  contas_a_pagar.models import Contas_Pagar
from  contas_a_pagar.api.serializers import Contas_Pagar_serializer

# segue o padrao junto com as bibliotecas importadas
class Contas_Pagar_viewsets(viewsets.ModelViewSet):
    queryset = Contas_Pagar.objects.all().order_by('-pago') # ordenar por status
    serializer_class = Contas_Pagar_serializer