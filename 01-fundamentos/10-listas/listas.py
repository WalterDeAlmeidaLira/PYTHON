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
print(listaJuntas)
listaJuntas.pop()
print(listaJuntas)
listaJuntas.insert(3,21)
print(listaJuntas)
listaJuntas.pop(3)
print(listaJuntas)

print("o valor 10 está na lista? ", end='')
print(10 in listaJuntas)

for i in listaJuntas:
    print(i)

