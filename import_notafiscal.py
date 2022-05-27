import csv
from apps.fornecedor.models import Fornecedor

def csv_to_list(filename: str) -> list:
    '''
    Lê um csv e retorna um OrdereDict.
    '''
    with open(filename) as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',')
        csv_data = [line for line in reader]
    return csv_data

def save_data(data):
    '''
    Salvar os dados no banco.
    '''
    aux = []
    for item in data:
        #status = True if item.get('status') == 'True' else False
        id_fornecedor = item.get('id')
        nome = item.get('nome')
        cnpj = item.get('cnpj')
        telefone = item.get('telefone')
        obj = Fornecedor(
            id=id_fornecedor,
            nome=nome,
            cnpj=cnpj,
            telefone=telefone,
        )
        aux.append(obj)
        Fornecedor.objects.bulk_create(aux)

data = csv_to_list('csv/fornecedor.csv')
save_data=(data)

