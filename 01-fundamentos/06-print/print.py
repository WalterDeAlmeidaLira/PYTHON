nome = input("Digite seu nome ")
msg = "Olá " + nome + ". Bem-vindo ao Python!" 
print(msg)

print('imprime a msg e quebra a linha')
print('imprime a msg e não quebra a linha. ', end='')
print('Mesma linha!')

nome2 = "Fulano"
idade = 102
msg_formatada = "O nome dele(a) é {0} e ele(a) tem {1} anos.".format(nome2,idade) 
print(msg_formatada)

time = input("Digite seu time de  coração: ")
print(f"Seu time do coração é o {time}")
print(f'A soma de 1 mais 1 é igual {1+1}')

valor = 123.123456789
print(f'o valor é {valor:.2f}')
print(f'o valor é \'{valor:.2f}\'')
