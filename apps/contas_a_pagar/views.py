from django.shortcuts import redirect, render
from django.views.generic import (
            ListView, UpdateView,
            DeleteView,
            )
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.db.models import Q

from django.contrib import messages
from django.contrib.messages import constants

from .models import Contas_Pagar
from .forms import ContaPagarForm

def contas_pagar_list(request):
    queryset = request.GET.get('q')
    contas = Contas_Pagar.objects.all()

    if queryset:
        contas = Contas_Pagar.objects.filter(
            Q(fornecedor__nome__icontains=queryset)|
            Q(data_vencimento__icontains=queryset)
        )

    paginator = Paginator(contas, 9)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {
        'contas':contas,
        'posts':posts,
        #'filtrar':filtrar
    }
    return render(request, 'contas_a_pagar/contas_pagar_list.html', context)


class ContasPagarDelete(DeleteView):
    model = Contas_Pagar
    success_url = reverse_lazy('contas_pagar_list')


def contas_pagar_create( request):
    template_name = 'contas_a_pagar/contas_pagar_form.html'
    form = ContaPagarForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.add_message(request, constants.SUCCESS,' Conta cadastrada com sucesso!')
        return redirect(reverse_lazy('contas_pagar_list'))
    context={
        'form':form
    }
    return render(request, template_name, context)


class ContasUpdateView(UpdateView): 
    template_name = 'contas_a_pagar/nota_pagar_edit.html' 
    model = Contas_Pagar 
    fields = ['fornecedor', 'data_vencimento', 'pago', 'ids_notas_fiscais'] 
    success_url = reverse_lazy('contas_pagar_list')