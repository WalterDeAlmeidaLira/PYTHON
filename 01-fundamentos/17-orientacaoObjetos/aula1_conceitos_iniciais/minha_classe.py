class Minha_Classe:
    def __init__(self,info):
        self.atributo_1 = "teste"
        self.atributo_2 = info
        print(self.atributo_2)

    def metodo_1(self):
        print('minha primeira ação!')

#instância da classe
minha_classe = Minha_Classe("teste para informações!!")

#usando um metodo da classe 
minha_classe.metodo_1()
