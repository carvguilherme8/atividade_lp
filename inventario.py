from excecoes import ErroVenda, ErroRetorno

class Inventario():
    '''
    Classe que representa o inventário
    '''
    def __init__(self):
        """
        Construtor para inicializar um objeto inventário. Cria um estoque e um caixa.
        """
        self.estoque = {'laptop': [], 'tablet': [], 'celular': []}
        self.caixa = 0

    def reposicao(self, prod, qtd_prod):
        """
        Repõe o estoque de um produto.

        Args:
            prod(object produto): objeto produto que será adicionado no estoque.
            qtd_prod(int): quatidade de produto a ser adicionado no estoque.
        """
        n = 0
        try:
            while n < qtd_prod:
                self.estoque[prod.tipo].append(prod.__str__())
                n += 1
        except:
            print("Não foi possivel adicionar o item no estoque")

    def venda_produto(self, prod, qtd_prod):
        """
        Vende um produto que está no estoque e adiciona o seu valor ao caixa.

        Args:
            prod(object produto): objeto produto que será vendido.
            qtd_prod(int): quatidade de produto a ser vendido.
        """
        if len(self.estoque[prod.tipo]) >= qtd_prod:
            n = 0
            while n < qtd_prod:
                self.estoque[prod.tipo].pop()
                self.caixa += prod.valor
                n += 1
        else:
            raise ErroVenda()

    def retorno_produto(self, prod, qtd_prod):
        """
        Retorna o produto ao estoque, devolvendo o dinheiro.

        Args:
            prod(object produto): objeto produto que será adicionado novamente ao estoque.
            qtd_prod(int): quatidade de produto que retornará ao estoque.
        """
        if self.caixa >= prod.valor*qtd_prod:
            self.caixa -= prod.valor
            self.estoque[prod.tipo].append(prod.__str__())
        else:
            raise ErroRetorno