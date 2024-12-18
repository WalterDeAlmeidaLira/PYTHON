leitor = open('texto.txt','r')

exibir = leitor.read()

print(exibir.replace('teste',"troquei"))
print(exibir.split('\n'))
print(type(exibir))
