import math

# funcoes builtin - internas do python

valores = [-2,5,-8,10,-15,100,58,0]
print(f'maior valor {max(valores)}')
print(f'menor valor {min(valores)}')

a = -10
b = 5

print(f'valor absoluto: {abs(a)}')
print(f'potência: {pow(a,2)}')

c = 0.2546695

print(f'Arredondamento: {round(c,3)}')

# módulo para funcoes matemáticas

x = 8 
y = 100

raiz_quadrada = math.sqrt(x)
print(f'Raiz quadraada: {raiz_quadrada}')
print(f'Arredondamento para cima {math.ceil(raiz_quadrada)}')
print(f'Arredondamento para baixo {math.floor(raiz_quadrada)}')
