from excecoes import ErroVenda, ErroRetorno

class Inventario():
    '''
    Classe que representa o inventário
    '''
    def __init__(self):
        self.estoque = []
        self.caixa = 0

    def reposicao(self, prod, qtd_prod):
        self.estoque.append(prod)
        self.estoque[prod] += qtd_prod
        else:
            self.estoque[prod] = qtd_prod
    #cria a chave no dicionario e adiciona o qtd ou apenas soma a qtd caso chave (produto) exista

    def venda_produto(self, prod, qtd_prod):
        if prod in self.estoque and self.estoque[prod] >= qtd_prod:
            self.estoque[prod] -= qtd_prod #subtrai valor (qtd) da chave (produto) do dicionario
            self.caixa += prod.valor*qtd_prod #add dinheiro no caixa
        else:
            raise ErroVenda()

    def retorno_produto(self, prod, qtd_prod):
        if prod in self.estoque:
            self.estoque[prod] += qtd_prod
        else:
            self.estoque[prod] = qtd_prod

        if self.caixa >= valor*qtd_prod:
            self.caixa -= valor*qtd_prod
        else:
            raise ErroRetorno()
    #subtrai qtd do dicionario
    #retorna dinheiro ao cliente