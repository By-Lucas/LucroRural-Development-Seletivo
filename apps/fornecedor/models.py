from django.db import models
import uuid

class Csv(models.Model):
    file_name = models.FileField(upload_to='arquivos-csv')
    data_importacao = models.DateTimeField(auto_now=True)
    activated = models.BooleanField(default=False)
    class Meta:
        db_table = 'Csv'
    def __str__(self) -> str:
        return f"ID Filename {self.id}"

# Create your models here.
class Fornecedor(models.Model):
    id = models.UUIDField(primary_key=True) #default=uuid.uuid4, editable=False
    nome = models.CharField(max_length=100, null=False, blank=False)
    cnpj = models.CharField(max_length=18, null=False, blank=False)
    telefone = models.CharField(max_length=15, null=False, blank=False)
    data_cadastro = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Fornecedor'
        verbose_name  = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'
        managed = True
        #unique_together = ('id', 'pago') Tabelas com id ou informações unicas
    
    def __str__(self) -> str:
        return self.nome