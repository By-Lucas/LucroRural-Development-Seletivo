import requests
import os
import sys

#nome = input('\n\nQual NOME do paciente: ')

def consumir_api():
    r = requests.get('http://127.0.0.1:8000/api/fornecedor')
    # Convertendo dados
    data = r.json()

    for testar_api in data:
        #if testar_api['nome'] == nome :
        print('\n\nID: ',testar_api['id'])
        print('NOME: ',testar_api['nome'])
        print('cnpj: ',testar_api['cnpj'])
        print('telefone: ',testar_api['telefone'])
        print('data_cadastro: ',testar_api['data_cadastro'])

if __name__ == '__main__':
    consumir_api()