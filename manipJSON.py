dict = {
    'nome': 'Guid Van Rossum',
    'linguagem': 'Python',
    'similar': ['c','Modula-3','lisp'],
    'users': 1000000
}

# Converter para JSON:
import json
new = json.dumps(dict)

# Para gravar o arquivo:
with open('arquivos/dados2.json','w') as arq:
    arq.write(new)

# Para Ler o arquivo
with open('arquivos/dados2.json','r') as arq:
    texto = arq.read()
    data = json.loads(texto)
    print(data)

#Copiar dados de um arquivo para outro:
import os
fonte = 'arquivos/dados.json' 
destino = 'arquivos/dados2.json'

with (fonte,'r') as infile:
    text = infile.read()
    with (destino,'w') as output:
        output.write(text)
