# A função zip recebe duas sequencias e retorna em uma outra sequência de tuplas
# O número de tuplas é o tamnho da menor sequência, excluindo os excedentes da maior

seq1 = ['voz', 'teclado', 'baixo', 'Guitarra', 'Jacaré']
seq2 = ['Mickael', 'Jean', 'Gustavo', 'Cláudio']
seq3 = {'Teclado':'Jean', 'Guitarra':'Willkley'}
 
zipped = list(zip(seq1,seq2))
print(zipped)

enumerated = list(enumerate(seq1))
print(enumerated)

for i,item in enumerated:
    print(i,item)