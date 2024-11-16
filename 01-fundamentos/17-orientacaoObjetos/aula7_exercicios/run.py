class Loja:
    
    taxa = 1.1

    def __init__(self,valor:float) -> None:
        self.valor_produto_bruto = valor
        
    
    def consultar_valor_do_produto(self):
        return self.produto * self.taxa
    
    def editar_taxa_do_produto(self,taxa:float):
        self.taxa = taxa

