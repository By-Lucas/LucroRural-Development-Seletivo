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


class Fornecedor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    nome = models.CharField(max_length=100, null=False, blank=False, db_column='nome')
    cnpj = models.CharField(max_length=18, null=False, blank=False, db_column='cnpj')
    telefone = models.CharField(max_length=14, null=False, blank=False, db_column='telefone')
    data_cadastro = models.DateTimeField(auto_now=True)

    #colocar pontos e traços no CPF
    def get_cnpj(self):
        if self.cnpj:
            cnpj = str(self.cnpj)
            cnpj_parte_1 = cnpj[0:4]
            cnpj_parte_2 = cnpj[2:5]
            cnpj_parte_3 = cnpj[5:8]
            cnpj_parte_4 = cnpj[8:12]
            cnpj_parte_5 = cnpj[14:18]
            cnpj_formatado = f"{cnpj_parte_1}**.***/****-{cnpj_parte_5}"
            return cnpj_formatado

    def get_telefone(self):
        if self.telefone:
            telefone = str(self.telefone)
            telefone_parte_1 = telefone[0:7]
            telefone_parte_2 = telefone[12:14]
            telefone_formatado = f"{telefone_parte_1}*** - **{telefone_parte_2}"
            return telefone_formatado

    class Meta:
        db_table = 'Fornecedor'
        verbose_name  = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'
        managed = True
        #unique_together = ('id', 'pago') Tabelas com id ou informações unicas
    
    def __str__(self) -> str:
        return self.nome