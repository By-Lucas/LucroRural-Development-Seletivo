from rest_framework import viewsets

from  notafiscal.models import Nota_Fiscal
from  notafiscal.api.serializers import  Nota_Fiscal_Serializer

class  Nota_Fiscal_viewsets(viewsets.ModelViewSet):
    queryset = Nota_Fiscal.objects.all() # pegar todos os registros
    serializer_class =  Nota_Fiscal_Serializer # pegar os serializers