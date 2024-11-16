class MinhaClasse:
    estatico = "teste1"

my_class = MinhaClasse()
my_class2 = MinhaClasse()

print(MinhaClasse.estatico)
print(my_class.estatico)
print(my_class2.estatico)

MinhaClasse.estatico = "mudei o teste"

print(MinhaClasse.estatico)
print(my_class.estatico)
print(my_class2.estatico)

#criando um espelho para classe my_class - noa sofre mais altecao da class, pois é um espelho da classe MinhaClasse
my_class.estatico = "criei um espelho!"

print(MinhaClasse.estatico)
print(my_class.estatico)
print(my_class2.estatico)
