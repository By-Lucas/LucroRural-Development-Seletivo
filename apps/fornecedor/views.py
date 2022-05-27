from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.messages import constants
from .models import Fornecedor, Csv
from .forms import CsvForm
import csv, io
# Create your views here.

def export_csv(request):
    queryset = Fornecedor.objects.all()

    options = Fornecedor._meta
    fields = [field.name for field in options.fields]

    responde = HttpResponse(content_type='text/csv')
    responde['Content-Disposition'] = "atachment; filename:'fornecedor.csv'"

    write = csv.writer(responde)

    write.writerow([options.get_field(field).verbose_name for field in fields])

    for obj in queryset:
        write.writerow([getattr(obj, field) for field in fields])

    return responde

def import_csv(request):
    if request.method == 'POST':
        filename = request.get('import_file')#'csv/fornecedor.csv'
        print(filename)
        fornecedores = []
        with open(filename, "r") as csv_file:
            data = list(csv.reader(csv_file, delimiter=";"))
            for row in data[1:]:
                fornecedores.append(Fornecedor(
                    id=row['id'],
                    nome=row['nome'],
                    cnpj=row['cnpj'],
                    telefone=row['telefone']
                ))
        if len(fornecedores) > 0:
            Fornecedor.objects.bulk_create(fornecedores)
    else:
        print('Algo deu errado')

    return redirect('/')

def upload_file_view(request):
    fornecedor = Fornecedor.objects.all()
    
    form = CsvForm(request.POST, request.FILES or None)

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
        'form':form
    }
    return render(request, 'upload_file.html',context)
