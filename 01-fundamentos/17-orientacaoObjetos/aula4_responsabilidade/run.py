class MinhaClasse:
    def __init__(self):
        print("objeto criado!")
    
    def cadastraUsuario(self, nome, idade):
        if self.verificadorDeTipo(nome,idade):
            self.registrador(nome,idade)
        else:
            self.erroCadastro()
    
    def verificadorDeTipo(self,nome,idade):
        return isinstance(nome,str) and isinstance(idade,int)

    def registrador(self,nome,idade):
        print('acessandoo banco de dados aguarde...')
        print(f'cadastrando com nome {nome} e idade {idade}')

    def erroCadastro(self):
        print("erro no cadastro!!")

my_class = MinhaClasse()
my_class.cadastraUsuario('teste',19)