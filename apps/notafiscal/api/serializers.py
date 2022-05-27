from  rest_framework import serializers

from notafiscal.models import Nota_Fiscal


class Nota_Fiscal_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Nota_Fiscal # Usar sempre este modelo
        fields = '__all__' # pegar todos os campos da classe pacientes importada