num = int(input('Informe o número de alunos: '))
c = 1
alunos = {}
# aprov = {}
# recup = {}
# reprov = {}

while (c<=num):
    nome = input('Nome do aluno: ')
    nota = float(input('Nota de {}: '.format(nome)))
    alunos[nome] = nota
    c+=1
med = (sum(alunos.values())/num)

for aluno in alunos.items():
    print(aluno)

print('A média da turma é', med)
