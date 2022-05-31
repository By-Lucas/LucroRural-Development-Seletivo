from django.contrib import admin
from .models import Contas_Pagar
from import_export.admin import ImportExportModelAdmin


@admin.register(Contas_Pagar)
class ContasAdmin(ImportExportModelAdmin):
    list_display= ('id', 'data_vencimento', 'pago')