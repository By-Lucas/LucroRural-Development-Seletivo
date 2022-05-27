from django.http import HttpResponse
from django.shortcuts import render
from fornecedor.models import Fornecedor

import csv

# Create your views here.
def index(request):
    fornecedor = Fornecedor.objects.all()
    context = {
        'fornecedor':fornecedor,
    }
    return render(request, 'index.html', context)
