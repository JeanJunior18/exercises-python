#Falta deparar os arquivos das listas que ficam salvas no arquivo CSV

dados = {'Nome': None,'Idade': None, 'Média': None}
alunos = []
idade = []
media = []
nalunos = int(input('Insira o número de alunos: '))
c = 1

while(c<=nalunos):
    print('Recebendo dados do {}° aluno, por favor leia com atenção.'.format(c))
    aluno = input('Nome do aluno: ')
    age = int(input('Idade de '+ aluno+': '))
    n1 = float(input('Informe a nota da 1° rova: '))
    n2 = float(input('Informe a nota da 2° rova: '))
    med = (n1+n2)/2
    alunos.append(aluno)
    dados['Nome'] = alunos
    idade.append(age)
    dados['Idade'] = idade
    media.append(med)
    dados['Média'] = media
    c+=1

fileName = input('Digite o nome do arquivo para salvar os dados: ')
fileName = fileName+'.csv'
import csv
with open(fileName,'w') as arq:
    learn = csv.writer(arq)
    for line in dados.items():
        learn.writerow(line)
        
with open(fileName,'r') as arq:
    ler = csv.reader(arq)
    ler = list(ler)


arq = open(fileName,'r')
data = arq.read()
print(data)

