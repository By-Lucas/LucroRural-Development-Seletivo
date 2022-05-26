from django.db import models
import uuid

# Create your models here.
class Fornecedor(models.Model):
    id = models.UUIDField(primary_key=True,  default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=100, null=False, blank=False)
    cnpj = models.CharField(max_length=14, null=False, blank=False)
    telefone = models.CharField(max_length=11, null=False, blank=False)
    data_cadastro = models.DateTimeField(auto_now=True)

