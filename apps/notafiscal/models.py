from statistics import mode
from django.db import models
import uuid
from fornecedor.models import Fornecedor

class Nota_Fiscal(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid5)
    numero_da_conta = models.CharField(max_length=10, null=False, blank=False)
    fornecedor_ = models.BooleanField(Fornecedor)
    data_emissao_not = models.DateTimeField(auto_now=True, editable=True)
    nome_produto = models.CharField(max_length=50, null=False, blank=False)
    categoria = models.CharField(max_length=20, null=False, blank=False)
    quantidade = models.DecimalField(decimal_places=2, null=False, blank=False)
    valor_total = models.DecimalField(decimal_places=2, null=False, blank=False)




