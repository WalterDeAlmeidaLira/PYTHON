class Minha_classe:

    estatico = "Lhama"

    def __init__(self,estado)->None:
        self.estado = estado
    
    def print_variavel_de_classe(self):
        print(self.estatico)
    
    @classmethod # decorador que faz o método ser da classe e não só da instância.
    def alteracao_da_variavel_de_classe(cls):
        cls.estatico = "algumaCoisa"

obj1 = Minha_classe(True)
obj2 = Minha_classe(True)

obj1.alteracao_da_variavel_de_classe()
print(Minha_classe.estatico)
print(obj1.estatico)
print(obj2.estatico)

