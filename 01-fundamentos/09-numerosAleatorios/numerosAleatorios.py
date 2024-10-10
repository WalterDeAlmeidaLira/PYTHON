import random 

for i in range(0,5):
    n = random.randint(1,50)
    print(f'Número gerado: {n}')

decimal = random.random()
print(f'Número aleatório {round(decimal * 10,2)}')

print(f'uniforme {random.uniform(1,10)}')

sorteio = [1,2,3,4,5]

selecionado = random.choice(sorteio)

print(f'Número selecionado {selecionado}')

amostra = random.sample(sorteio,3)

print(f'Amostra: {amostra}')

print(f'lista original {sorteio}')
embaralha = random.shuffle(sorteio)
print(f'lista embaralhada {sorteio}')