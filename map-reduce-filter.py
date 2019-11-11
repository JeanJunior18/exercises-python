# Função Map recebe uma função e uma sequência e opera a sequẽcia na função. Ex:

def fahrenheit(T):
    return ((float(9)/5)*T+32)

temperaturas = [0,22.5,40,100]

temp = map(fahrenheit, temperaturas)
temp = list(temp)
print(temp)

# Pode ser usado para somar listas. Ex:
a = [1,2,3,4,5]
b = [5,4,3,2,1]

sum = map(lambda x,y: x+y, a, b) # Este caso usa uma função anônima
sum = list(sum)
print(sum)


# Função Reduce recebe os mesmos valores que a Map e executa a função 
from functools import reduce
def soma(x,y):
    return x+y

lista = [47,11,42,13]

red = reduce(soma,lista)
print(red)

# Filtra todos os elemetos de uma sequência que retornam true

def verificaPar(num):
    if num%2==0:
        return True
    else:
        return False

lista = [0,1,2,3,4,5,6,7,8,9,10]
test = filter(verificaPar,lista)
print(list(test))
