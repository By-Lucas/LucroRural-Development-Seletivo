from rest_framework import serializers

from  contas_a_pagar.models import Contas_Pagar

# esse segue um padrao simples

class  Contas_Pagar_serializer(serializers.ModelSerializer):
    class Meta:
        ordering = ['-id']
        model = Contas_Pagar
        fields = ("id", "fornecedor", "data_vencimento", "pago", "ids_notas_fiscais")
        extra_kwargs = {'books': {'required': False}}