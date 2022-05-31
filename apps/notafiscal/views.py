from django.shortcuts import render, redirect, HttpResponse
from django.core.paginator import Paginator
from django.db.models import Q
from django.urls import reverse_lazy

from django.contrib import messages
from django.contrib.messages import constants

from .models import Nota_Fiscal, Csv_notas
from .forms import CsvNotaForm, NotaFiscalForm
import csv


def notas_fiscais(request):
    nota_fiscal = Nota_Fiscal.objects.all().order_by('nome_produto')
    form = CsvNotaForm(request.POST, request.FILES or None)

    queryset = request.GET.get('q')
    if queryset:
        nota_fiscal = Nota_Fiscal.objects.filter(
            Q(numero_da_nota__icontains=queryset)|
            Q(fornecedor__icontains=queryset)|
            Q(nome_produto__icontains=queryset)|
            Q(categoria__icontains=queryset)
        )

    paginator = Paginator(nota_fiscal, 9)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    if form.is_valid():
        form.save()
        form = CsvNotaForm()
        obj = Csv_notas.objects.get(activated=False)
        fornecedores = []
        with open(obj.file_name.path, "r", encoding="utf-8") as csv_file:
            data = list(csv.reader(csv_file, delimiter=";"))
            for rows in data[1:]:
                fornecedores.append(rows)
            for row in fornecedores:
                data = row[2]
                n1 = f'{data[8:10]}/{data[5:7]}/{data[0:4]}'
                if len(row) > 0:
                    Nota_Fiscal.objects.update_or_create(
                        numero_da_nota=row[0],
                        fornecedor=row[1],
                        data_emissao_nota=row[2],
                        nome_produto=row[3],
                        categoria=row[4],
                        quantidade=row[5],
                        valor_total=row[6]
                        )
            obj.activated = True
            obj.save()
            messages.add_message(request, constants.SUCCESS, 'Importação feita com sucesso')
            return redirect('notas_fiscais')
    context = {
        'nota_fiscal':nota_fiscal,
        'form':form,
        'posts':posts
    }
    return render(request, 'notafiscal/notas_fiscais.html',context)

def export_notas_csv(request):
    queryset = Nota_Fiscal.objects.all()
    options = Nota_Fiscal._meta
    fields = [field.name for field in options.fields]
    responde = HttpResponse(content_type='text/csv')
    responde['Content-Disposition'] = "atachment; filename:'fornecedor.csv'"
    write = csv.writer(responde)
    write.writerow([options.get_field(field).verbose_name for field in fields])
    for obj in queryset:
        write.writerow([getattr(obj, field) for field in fields])
    return responde

def NotasFiscaisCreate(request):
    form  = NotaFiscalForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save() 
            messages.success(request, 'Novo fornecedor cadastrado com sucesso!')
            return redirect('all_fornecedores')
        else:
            messages.error(request, 'Novo fornecedor nao foi cadastrodo!')
            return redirect('Create_Fornecedor')
    return render(request, 'notafiscal/notasfiscais_form.html',{'form':form})