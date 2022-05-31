from django.db import models
from fornecedor.models import Fornecedor
from notafiscal.models import Nota_Fiscal
import uuid

class Contas_Pagar(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE, null=True, db_column='fornecedor')
    data_vencimento = models.DateField(null=False, blank=False)
    pago = models.BooleanField(default=False)
    ids_notas_fiscais = models.ManyToManyField(Nota_Fiscal)

    class Meta:
        db_table = 'Contas_pagar'
        verbose_name  = 'Contas_pagar'
        verbose_name_plural = 'Contas_pagar'
        managed = True

    def __str__(self) -> str:
        return f'ID Conta: {self.id}'