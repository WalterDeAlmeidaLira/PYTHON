nota1 = float(input("DIGITE A PRIMEIRA NOTA: ")) 
nota2 = float(input("DIGITE A SEGUNDA NOTA: "))

media = (nota1 + nota2) / 2

if(media >= 7 ): 
    print("Aluno(a) aprovado(a)!")
elif(media >= 5):
    print("Aluno(a) em recuperação!")
else: 
    print("Reprovado(a)!")

print("Sua média é {}".format(media))