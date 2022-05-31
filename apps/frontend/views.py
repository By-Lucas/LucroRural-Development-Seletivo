from django.shortcuts import render
from fornecedor.models import Fornecedor


def index(request):
    return render(request, 'index.html')
