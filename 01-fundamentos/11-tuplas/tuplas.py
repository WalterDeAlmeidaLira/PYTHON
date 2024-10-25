# são imutáveis
lista = (2,4,5,6,7,2,5,6,4)

print(lista)
print(f'tamanho da lista: {len(lista)}')
print(f'quantas vezes o numero 4 se repete: {lista.count(4)}')
print(f'o numero 2 está presente na lista: {2 in lista}')
print(f'soma todos os valores: {sum(lista)}')

# nao pode usar nenhum método que altere qualquer coisa na tupla 
listaMutavel = list(lista)
listaMutavel.append(25)
print(f'lista mutável {listaMutavel}')
print(f'nao estou modificando a tupla {sorted(lista)}')