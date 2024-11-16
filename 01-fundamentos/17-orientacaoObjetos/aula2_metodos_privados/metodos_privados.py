class Pessoa:
    def __init__(self,altura,cpf):
        self.altura = altura
        self.__cpf = cpf
    
    def apresentacao(self):
        print("altura = " + self.altura)
        print("cpf = "+ self.__cpf)

pessoa = Pessoa("1.78",'5648645634534')

pessoa.apresentacao()