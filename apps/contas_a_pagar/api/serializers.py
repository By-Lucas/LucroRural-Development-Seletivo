from rest_framework import serializers

from  contas_a_pagar.models import Contas_Pagar

# esse segue um padrao simples

class  Contas_Pagar_serializer(serializers.ModelSerializer):
    class Meta:
        model = Contas_Pagar
        fields = '__all__'