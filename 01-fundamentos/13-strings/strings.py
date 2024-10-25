frase = 'eu gosto de python'

#separa string com base em um caracter
palavras = frase.split()
print(palavras)

#busca um caracter na string e retorna o indice da primeira ocorrência
busca = frase.find('o')
print(busca)

print(f"caixa alta: {frase.upper()}")
print(f"caixa baixa: {frase.lower()}")
print(f"caixa somente a primeira palavra em caixa alta: {frase.capitalize()}")
print(f"primeira de cada palavra em caixa alta: {frase.title()}")

java = frase.replace('python','java')
print(java)

nome = '    um pálido ponto azul     '
print(f'com espaços {nome}')
print(f'sem a esquerda espaços {nome.lstrip()}')
print(f'sem a direita espaços {nome.rstrip()}')
print(f'sem espaços {nome.strip()}')

print(f'começa com e: {java.startswith('e')}')
print(f'acaba com a: {java.endswith('a')}')

"""
TEXTO DE DOCUMENTAÇÃO

"""