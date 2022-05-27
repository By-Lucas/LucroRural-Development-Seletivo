from  rest_framework import serializers

from fornecedor.models import Fornecedor

class  Fornecedor_serializer(serializers.ModelSerializer):
    class Meta:
        model = Fornecedor
        fields = '__all__'