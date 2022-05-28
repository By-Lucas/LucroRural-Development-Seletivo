from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import (
            ListView, UpdateView,
            DeleteView, CreateView,TemplateView
            )

from django.contrib import messages
from django.contrib.messages import constants

from .models import Fornecedor, Csv_notas
from .forms import CsvNotaForm, NotaFiscalForm
import csv



def all_fornecedores(request):
    fornecedor = Fornecedor.objects.all().order_by('nome')
    form = CsvForm(request.POST, request.FILES or None)
    paginator = Paginator(fornecedor, 9)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    if form.is_valid():
        form.save()
        form = CsvForm()
        obj = Csv.objects.get(activated=False)
        with open (obj.file_name.path, 'r') as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                if i == 0:
                    pass
                else:
                    import_fornecedores = Fornecedor.objects.update_or_create(
                        id=row[0],
                        nome=row[1],
                        cnpj=row[2],
                        telefone=row[3]
                    )
            obj.activated = True
            obj.save()
            messages.add_message(request, constants.SUCCESS, 'Importação feita com sucesso')
            return redirect('/')
    context = {
        'fornecedor':fornecedor,
        'form':form,
        'posts':posts
    }
    return render(request, 'all_fornecedores.html',context)

def FornecedorCreate(request):
    form  = FornecedorForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save() 
            messages.success(request, 'Novo fornecedor cadastrado com sucesso!')
            return redirect('all_fornecedores')
        else:
            messages.error(request, 'Novo fornecedor nao foi cadastrodo!')
            return redirect('Create_Fornecedor')

    return render(request, 'fornecedor/fornecedor_form.html',{'form':form})