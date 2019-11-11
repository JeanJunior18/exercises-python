import csv
with open('arquivos/numeros.csv','w') as arq:
    escritor = csv.writer(arq)
    escritor.writerow(('First','Second','Third'))
    escritor.writerow((18,20,19))
    escritor.writerow((1,0,1))

with open('arquivos/numeros.csv','r') as arq:
    leitor = csv.reader(arq)
    for x in leitor:
        print('O número de colunas é {}'.format(len(x)))
        print(x)

with open('arquivos/numeros.csv','r') as arq:
    leitor = csv.reader(arq)
    leitor = list(leitor)
    print(leitor)
