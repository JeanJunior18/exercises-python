#Cria um arquivo TXT automáticamente utilizando o Python "puro"

fileName = input("Insert the file name: ")
fileName = '../' + fileName + '.txt'
arq1 = open(fileName,"w")
text = input("Write the text: ")
arq1.write(text)
arq1.close()
read = open(fileName,"r")
print(read.read())
read.close()
