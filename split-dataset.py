#Separa os itens do dataset por linha em uma lista utilizando o python "puro"

arqcsv = open("../arquivos/salarios.csv","r")
data = arqcsv.read()
rows = data.split('\n')
full = []

for row in rows:
    spl = row.split(',')
    full.append(spl)

for item in full:
    print(item)

arqcsv.close()
