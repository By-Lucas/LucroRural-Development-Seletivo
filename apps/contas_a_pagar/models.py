from django.db import models
from fornecedor.models import Fornecedor
from notafiscal.models import Nota_Fiscal
import uuid

class Contas_Pagar(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    Fornecedor = models.ManyToManyField(Fornecedor)
    data_vencimento = models.DateField(null=False, blank=False)
    pago = models.BooleanField(default=False)
    ids_notas_fiscais = models.ManyToManyField(Nota_Fiscal)

    class Meta:
        db_table = 'Contas_Pagar'
        verbose_name  = 'Contas_Pagar'
        verbose_name_plural = 'Contas_Pagar'
        managed = True
        #unique_together = ('id', 'pago') Tabelas com id ou informações unicas

    def __str__(self) -> str:
        return self.Fornecedor