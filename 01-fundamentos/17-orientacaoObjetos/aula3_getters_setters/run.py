class MinhaClass:
    def __init__(self) -> None:
        self.valor = 10
    
    def setterValor(self,valor):
        self.valor = valor
    
    def getterValor(self):
        return self.valor
    
my_class = MinhaClass()

retorno = my_class.getterValor()

print(retorno)

my_class.setterValor(15)

print(my_class.getterValor())
