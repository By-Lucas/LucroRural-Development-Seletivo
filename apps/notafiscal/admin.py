from django.contrib import admin
from .models import Nota_Fiscal, Csv_notas
from import_export.admin import ImportExportModelAdmin


admin.site.register(Csv_notas)

@admin.register(Nota_Fiscal)
class NotaAdmin(ImportExportModelAdmin):
    list_display = ('numero_da_nota', 
                'fornecedor', 
                'nome_produto', 
                'categoria', 
                'quantidade',
                'valor_total'
                )

