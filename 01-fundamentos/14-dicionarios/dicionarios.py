carro = {
    'marca':'honda',
    'modelo':'civic',
    'ano':2024
}

print("retorna as chaves de um dicionário ",carro.keys())
print("retorna os valores de um dicionário ",carro.values())
print(f'carro: {carro["modelo"]}')

for i in carro.keys():
    print(i)

for i in carro.values():
    print(i)

for x,y in carro.items():
    print(x,y)