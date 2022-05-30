from django.contrib import admin
from .models import Fornecedor, Csv
from import_export.admin import ImportExportModelAdmin


admin.site.register(Csv)

@admin.register(Fornecedor)
class FornecedorAdmin(ImportExportModelAdmin):
    list_display = ('id', 'nome', 'cnpj', 'telefone', 'data_cadastro')
