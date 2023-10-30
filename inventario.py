from excecoes import ErroVenda, ErroRetorno

class Inventario():
    '''
    Classe que representa o inventário
    '''
    def __init__(self):
        self.estoque = {'laptop': [], 'tablet': [], 'celular': []}
        self.caixa = 0

    def reposicao(self, prod, qtd_prod):
        n = 0
        try:
            while n < qtd_prod:
                self.estoque[prod.tipo].append(prod.__str__())
                n += 1
        except:
            print("Não foi possivel adicionar o item no estoque")

    def venda_produto(self, prod, qtd_prod):
        if len(self.estoque[prod.tipo]) >= qtd_prod:
            n = 0
            while n < qtd_prod:
                self.estoque[prod.tipo].pop()
                self.caixa += prod.valor*qtd_prod 
                n += 1
        else:
            raise ErroVenda()

    def retorno_produto(self, prod, qtd_prod):
        if self.caixa >= prod.valor*qtd_prod:
            self.caixa -= prod.valor*qtd_prod
            self.estoque[prod.tipo].append(prod.__str__())
        else:
            raise ErroRetorno




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