lista = [5,7,8,10]

lista2 = [7,4,6,9]

listaJuntas = lista + lista2

print(listaJuntas)

print(f'comprimento da lista: ', len(listaJuntas))
print(f'Ordena lista menor para maior: ', sorted(listaJuntas))
print(f'Ordena lista maior para menor: ', sorted(listaJuntas,reverse=True))
print(f'soma:', sum(listaJuntas))
print(f'mínimo:', min(listaJuntas))
print(f'máximo:', max(listaJuntas))

listaJuntas.append(12)
print("adicionadno 12: ",listaJuntas)
listaJuntas.pop()
print("removendo 12: ",listaJuntas)
listaJuntas.insert(3,21)
print("adicionadno 21 na posição 3: ",listaJuntas)
listaJuntas.pop(3)
print("removendo elemento da posição 3: ",listaJuntas)

print("o valor 10 está na lista? ", end='')
print(10 in listaJuntas)

for i in listaJuntas:
    print(i)

print("adicionando mais de um elemento")
nomes = ["joao","paulo","ricardo"]
nomes.extend(['felipe','emerson'])

print("lista de nomes: ",nomes)