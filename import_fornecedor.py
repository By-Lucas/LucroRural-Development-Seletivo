# Outro metodos de importar csv
def import_csv(request):
    if request.method == 'POST':
        filename = request.FILES['import_file']#'csv/fornecedor.csv'
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
        elif fornecedores:
            Fornecedor.objects.bulk_update(fornecedores)
    else:
        print('Algo deu errado')
    return redirect('/')
