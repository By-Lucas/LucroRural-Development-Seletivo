import csv

filename = 'notafiscal.csv'
#print(filename)
fornecedores = []
with open(filename, "r") as csv_file:
    data = list(csv.reader(csv_file, delimiter=";"))
    for row in data[1:]:
        fornecedores.append(row)
        #print(fornecedores["numero_nota"])
    for i in fornecedores:
        data = i[2]
        n1 = f'{data[8:10]}/{data[5:7]}/{data[0:4]}'
        print(n1)

if len(fornecedores) > 0:
    pass