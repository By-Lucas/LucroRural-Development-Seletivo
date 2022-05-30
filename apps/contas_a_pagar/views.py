from multiprocessing import context
from django.shortcuts import redirect, render
from django.views.generic import (
            ListView, UpdateView,
            DeleteView, CreateView,TemplateView
            )
from django.urls import reverse_lazy
from django.core.paginator import Paginator
# Alertas de messagens
from django.contrib import messages
from django.contrib.messages import constants

from .models import Contas_Pagar
from .forms import ContaPagarForm



def contas_pagar_list(request):
    contas = Contas_Pagar.objects.all().order_by('data_vencimento')
    paginator = Paginator(contas, 9)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {
        'contas':contas,
        'posts':posts
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