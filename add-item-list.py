num = int(input("Digite o número de alunos: "))
c = 1
alunos = []
while(c<=num):
    nome = input('Insira o nome do {}° aluno: '.format(c))
    alunos.append(nome)
    c+=1

alunos.sort()

for aluno in alunos:
    print(aluno)
