nome = "teste"
numero = 10
teste = True 
decimal = 10.5

nome_variaveis = "teste"
nomeComNumero2 = 42

n1 = n2 = n3 = n4 = 0.5

uma , duas = "tudo certo", 25

print(nome)
print(numero)
print(teste)
print(decimal)

print(nome_variaveis)
print(nomeComNumero2)

print(n1)
print(n2)
print(n3)
print(n4)

print(uma)
print(duas)

# FUNÇÃO TYPE - retorna o tipo da variável

print(type(nome))
print(type(numero))
print(type(teste))
print(type(decimal))

#  FUNÇÃO ISINSTANCE - retorna true ou false

print(isinstance(n1,float))
print(isinstance(nome,str))
print(isinstance(teste,bool))
print(isinstance(teste,float))
print("Duas verificações juntas - int ou float ",isinstance(n1,(int,float)))

