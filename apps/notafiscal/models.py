from django.db import models
import uuid
from fornecedor.models import Fornecedor
from multiselectfield import MultiSelectField

class Csv_notas(models.Model):
    file_name = models.FileField(upload_to='notas-csv')
    data_importacao = models.DateTimeField(auto_now=True)
    activated = models.BooleanField(default=False)
    class Meta:
        db_table = 'Csv_notas'
    def __str__(self) -> str:
        return f"ID Filename {self.id}"


class Nota_Fiscal(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    numero_da_conta = models.CharField(max_length=10, null=False, blank=False)
    fornecedor = models.ManyToManyField(Fornecedor)
    data_emissao_nota = models.DateTimeField(auto_now=True, editable=True)
    nome_produto = models.CharField(max_length=50, null=False, blank=False)
    categoria = models.CharField(max_length=20, null=False, blank=False)
    quantidade = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)

    class Meta:
        managed = True
        db_table = 'Nota_Fiscal'
        verbose_name  = 'Nota_Fiscal'
        verbose_name_plural = 'Notas_Fiscais'
        #unique_together = ('id', 'pago') Tabelas com id ou informações unicas

    def __str__(self) -> str:
        return self.nome_produto

